#-*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ABPItem(scrapy.Item):
    AcadYear = scrapy.Field()
    Semester = scrapy.Field()
    ModuleCode = scrapy.Field()
    ModuleTitle = scrapy.Field()
    StudentAcctType = scrapy.Field()
    AveragePoints = scrapy.Field()
