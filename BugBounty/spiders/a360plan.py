# -*- coding: utf-8 -*-

import scrapy
from BugBounty.items import BugbountyItem


class A360planSpider(scrapy.Spider):
    name = '360plan'
    allowed_domains = ['360.cn']
    start_urls = ['http://loudong.360.cn/Reward/plan']

    def parse(self, response):
        for line in response.xpath('//div[@class="companyList2"]'):
            item = BugbountyItem()
            item['projectUrl'] = line.xpath('./dl/dd/a/@href').extract()
            item['projectName'] = line.xpath('./dl/dd/a/text()').extract()
            item['minimumBounty'] = line.xpath('./dl/dd[2]/text()').extract()
            yield item
