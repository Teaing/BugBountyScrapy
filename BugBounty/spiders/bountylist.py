# -*- coding: utf-8 -*-

import scrapy
from BugBounty.items import BugbountyItem


class BountylistSpider(scrapy.Spider):
    name = 'bountylist'
    allowed_domains = ['bugcrowd.com']
    start_urls = ['https://www.bugcrowd.com/bug-bounty-list/']

    def parse(self, response):
        for line in response.xpath('//tbody/tr'):
            item = BugbountyItem()
            item['projectName'] = line.xpath('./td/a/text()').extract()
            item['projectUrl'] = line.xpath('./td/a/@href').extract()
            yield item
