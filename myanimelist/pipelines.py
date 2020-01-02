# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from myanimelist.items import AnimeItem, ReviewItem, ProfileItem

class MyAnimeListPipeline(object):

    def open_spider(self, spider):
      self.files = {}
      self.files['AnimeItem']   = open('data/animes.txt', 'w')
      self.files['ReviewItem']  = open('data/reviews.txt', 'w')
      self.files['ProfileItem'] = open('data/profiles.txt', 'w')

    def close_spider(self, spider):
      for k, v in self.files.items():
        v.close()

    def process_item(self, item, spider):
      item_class = item.__class__.__name__

      line =  json.dumps(dict(item)) + '\n'
      self.files[item_class].write(line)

      return item