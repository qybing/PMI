# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class CommunityPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        db_auth = self.client.admin
        db_auth.authenticate('laocheng', 'laocheng')
        self.db = self.client[self.mongo_db]


    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if item['sheet_name']:
            self.db[item['sheet_name']].update({'url': item['url']}, {'$set': dict(item)}, True)
        else:
            self.db[item['city']].update({'url': item['url']}, {'$set': dict(item)}, True)
        print(item)
        print('已经存进去了')
        return item
