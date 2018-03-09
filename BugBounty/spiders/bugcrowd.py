# -*- coding: utf-8 -*-

import scrapy
from BugBounty.items import BugbountyItem


class BugcrowdSpider(scrapy.Spider):
    name = 'bugcrowd'
    allowed_domains = ['bugcrowd.com']
    start_urls = ['https://bugcrowd.com/programs']

    def parse(self, response):
        nextLink = response.xpath('//li[@class="bc-pagination__item bc-pagination__item--next"]/a/@href').extract()
        for line in response.xpath('//div[@class="bc-program-card__header"]'):
            item = BugbountyItem()
            item['projectUrl'] = line.xpath('./a/@href').extract()
            item['projectName'] = line.xpath('./h4/a/text()').extract()
            if line.xpath('./span/text()').extract():
                item['openStatus'] = [line.xpath('./span/text()').extract()[0].replace('\n', '')]
            yield item
        if nextLink:
            yield scrapy.Request(response.urljoin(nextLink[0]), callback=self.parse)
