# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BugbountyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    projectType = scrapy.Field()
    projectName = scrapy.Field()
    projectUrl = scrapy.Field()
    openStatus = scrapy.Field()
    bugCount = scrapy.Field()
    minimumBounty = scrapy.Field()
    disclosureUrl = scrapy.Field()
    disclosureEmail = scrapy.Field()
