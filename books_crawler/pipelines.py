# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os


class BooksCrawlerPipeline(object):
    def process_item(self, item, spider):
        os.chdir('/media/pawan/Backup/SCRAPY/SCRAPED_IMAGES')
        if item['images'][0]['path']:
            new_image_name = item['title'][0] + '.jpeg'
            new_image_path = 'full/' + new_image_name
            os.rename(item['images'][0]['path'], new_image_path)

        return item
