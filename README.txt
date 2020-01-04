https://myanimelist.net/topanime.php?limit=<limit>

```
scrapy runspider myanimelist/spiders/MyAnimeList.py 
-a start_limit=<start_limit> 
-a end_limit=<end_limit> 
-s MONGODB_URL=<mongo_uri>
```