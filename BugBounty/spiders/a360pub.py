# -*- coding: utf-8 -*-

import json
import scrapy
from BugBounty.items import BugbountyItem


class A360pubSpider(scrapy.Spider):
    name = '360pub'
    allowed_domains = ['360.cn']
    start_urls = ['http://loudong.360.cn/Reward/pub']
    formData = {'s': '1', 'p': '1', 'token': ''}

    def parse(self, response):
        yield scrapy.FormRequest(response.url, formdata=self.formData, callback=self.getData)

    def getData(self, response):
        resultJson = json.loads(response.body)
        resultJsonData = resultJson.get('data')
        pageCount = int(resultJsonData.get('count'))
        nextPage = 1 + int(resultJsonData.get('current'))
        for line in resultJsonData.get('list'):
            item = BugbountyItem()
            item['projectName'] = line.get('company_name')
            item['projectType'] = line.get('industry')
            yield item
        if nextPage <= pageCount:
            self.formData['p'] = str(nextPage)
            yield scrapy.FormRequest(response.url, formdata=self.formData, callback=self.getData)
