# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SearchhousesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = scrapy.Field()
    lp_name = scrapy.Field()
    lp_alias = scrapy.Field()
    tags = scrapy.Field()
    price = scrapy.Field()
    kaipan = scrapy.Field()
    jiaofang = scrapy.Field()
    huxing = scrapy.Field()
    area = scrapy.Field()
    address = scrapy.Field()
    url = scrapy.Field()
    
    

    


    
