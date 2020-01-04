import numpy as np
from pymongo import MongoClient
import sys


mongodb_url = sys.argv[1]
fout    = open("images.csv", "w")
client  = MongoClient(mongodb_url)
db      = client['myanimelist']
      
cursor = db.animes.find(
    {}, {"_id": 0, "link": 1, "uid": 1, "img_url": 1})#.limit(10)

for doc in cursor:
  print(doc)
  fout.write("{},{}\n".format(doc['uid'], doc['img_url']))


fout.close()
