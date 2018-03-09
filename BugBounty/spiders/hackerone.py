# -*- coding: utf-8 -*-

import json
import scrapy
from BugBounty.items import BugbountyItem


class HackeroneSpider(scrapy.Spider):
    name = 'hackerone'
    allowed_domains = ['hackerone.com']
    start_urls = ['https://hackerone.com']

    def parse(self, response):
        contentUrl = 'programs/search?query=bounties:yes&sort=name:ascending&limit=1000'
        headers = {
            'x-requested-with': 'XMLHttpRequest',
            'Referer': 'https://hackerone.com/bug-bounty-programs'
        }
        replaceStr = response.url.replace('www.', '')
        yield scrapy.Request('{0}{1}'.format(replaceStr, contentUrl), headers=headers, callback=self.getData)

    def getData(self, response):
        jsonData = json.loads(response.body)
        for line in jsonData['results']:
            item = BugbountyItem()
            item['projectName'] = line.get('name')
            item['projectUrl'] = line.get('url')
            try:
                if line.get('meta').get('submission_state') == 'open':
                    item['openStatus'] = 'open'
                item['bugCount'] = line.get('meta').get('bug_count')
                item['minimumBounty'] = line.get('meta').get('minimum_bounty')
            except:
                item['openStatus'] = 'close'
            try:
                item['disclosureUrl'] = line.get('disclosure_url')
                item['disclosureEmail'] = line.get('disclosure_email')
            except:
                pass
            for line in item.keys():  # delete null value
                if not item.get(line):
                    item.pop(line)
            yield item
