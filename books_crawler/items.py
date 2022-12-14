# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class Books(Item):
    title = Field()
    price = Field()
    rating = Field()
    image_urls = Field()
    images = Field()
