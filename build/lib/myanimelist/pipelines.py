# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
from myanimelist.items import AnimeItem, ReviewItem, ProfileItem


class ProcessPipeline(object):

    def open_spider(self, spider):
      pass

    def close_spider(self, spider):
      pass

    def process_item(self, item, spider):
      item_class = item.__class__.__name__

      if item_class == "AnimeItem":
        item = self.process_anime(item)
      elif item_class == "ReviewItem":
        item = self.process_review(item)
      elif item_class == "ProfileItem":
        item = self.process_profile(item)

      return item

    def process_anime(self, item):
      item['score']      = float(item['score'].replace("\n", "").strip())
      item['ranked']     = int(item['ranked'].replace("#", "").strip())
      item['popularity'] = int(item['popularity'].replace("#", "").strip())
      item['members']    = int(item['members'].replace(",", "").strip())
      item['episodes']   = int(item['episodes'].replace(",", "").strip())

      return item

    def process_review(self, item):
      item['score']      = float(item['score'].replace("\n", "").strip())

      return item

    def process_profile(self, item):

      return item

class SaveLocalPipeline(object):

    def open_spider(self, spider):
      os.makedirs('data/', exist_ok=True)

      self.files = {}
      self.files['AnimeItem']   = open('data/animes.txt', 'w')
      self.files['ReviewItem']  = open('data/reviews.txt', 'w')
      self.files['ProfileItem'] = open('data/profiles.txt', 'w')

    def close_spider(self, spider):
      for k, v in self.files.items():
        v.close()

    def process_item(self, item, spider):
      item_class = item.__class__.__name__

      # Save
      self.save(item_class, item)

      return item

    def save(self, item_class, item):
      line =  json.dumps(dict(item)) + '\n'
      self.files[item_class].write(line)


class SaveMongoPipeline(object):

    def open_spider(self, spider):
      pass

    def close_spider(self, spider):
      pass

    def process_item(self, item, spider):
      item_class = item.__class__.__name__

      return item