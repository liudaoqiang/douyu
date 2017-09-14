# -*- coding: utf-8 -*-

import scrapy

class DouyuItem(scrapy.Item):
    nickname = scrapy.Field()
    imageurl = scrapy.Field()
    city = scrapy.Field()
