# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GaodepoiItem(scrapy.Item):
    # define the fields for your item here like:
    pois = scrapy.Field()
    pass
