# -*- coding: utf-8 -*-
import scrapy
import os

from douyu.settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline

class DouyuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['imageurl'])

    def item_completed(self, results, item, info):
        isok = results[0][0]
        if(isok):
            path = results[0][1]['path']
            nickname = item['nickname']
            city = item['city']
            old_path = IMAGES_STORE + path
            new_path = IMAGES_STORE + nickname + "_" + city + ".jpg"
            os.rename(old_path, new_path)
        return item

