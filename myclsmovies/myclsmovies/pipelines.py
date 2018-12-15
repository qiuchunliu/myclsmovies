# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
# 通过csv模块来写入csv文件


class MyclsmoviesPipeline(object):

    def __init__(self):
        self.file = open('myclsmovies.csv', 'a+')
        self.writer = csv.writer(self.file)

    def process_item(self, item, spider):
        # writerow 注意有两层括号
        self.writer.writerow((item['movie_ranking'],
                              item['movie_name'],
                              item['movie_time'],
                              item['movie_actor'],
                              item['movie_score'],
                              item['movie_link']))
        return item
