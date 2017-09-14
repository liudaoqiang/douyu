# -*- coding: utf-8 -*-
import scrapy
import json

from douyu.items import DouyuItem

class DouyuGirlSpider(scrapy.Spider):
    name = 'douyu_girl'
    allowed_domains = ['douyucdn.cn']

    base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalroom?limit=20&offset='
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        girl_list = json.loads(response.body)['data']
        if(len(girl_list) == 0):
            return
        for girl in girl_list:
            item = DouyuItem()
            item['imageurl'] = girl['vertical_src']
            item['nickname'] = girl['nickname']
            item['city'] = girl['anchor_city']

            yield item

        self.offset += 20
        url = self.base_url + str(self.offset)
        yield scrapy.Request(url, callback=self.parse)



