# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Xiao77Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ImageItem(scrapy.Item):
    image_id = scrapy.Field()
    image_title = scrapy.Field()
    image_type = scrapy.Field()
    image_link_head = scrapy.Field()
    image_link_tail = scrapy.Field()
    image_count = scrapy.Field()
    image_date = scrapy.Field()
    pass
