# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

import pymongo
logger = logging.getLogger(__name__)


class GaodepoiPipeline(object):
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
        if len(item['pois'])>0:
            logger.info('一共有{}个'.format(len(item['pois'])))
            self.db['Gaode_180905'].insert_many(item['pois'])
            logger.info('存入成功')
        return item
