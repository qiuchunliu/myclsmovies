# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyclsmoviesItem(scrapy.Item):
    # 通过设置，类似于创建字典里的键名通过实列化类
    # class Field(dict):
    movie_ranking = scrapy.Field()
    movie_name = scrapy.Field()
    movie_time = scrapy.Field()
    movie_actor = scrapy.Field()
    movie_link = scrapy.Field()
    movie_score = scrapy.Field()
