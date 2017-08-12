# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class Top100Pipeline(object):
    def __init__(self):
        client =  pymongo.MongoClient()
        top = client['top']
        self.inf = top['inf']

    def process_item(self, item, spider):
        _dict = dict(item)
        self.inf.insert(_dict)
        return item
