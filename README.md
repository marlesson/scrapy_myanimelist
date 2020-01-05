# myAnimeList Crawler

This crawler can crawl anime, reviews and profiles information from [myAnimeList](myAnimeList.net) using [Scrapy Framework](https://scrapy.org/)

## Usage

The main page to use for the crawler is 'https://myanimelist.net/topanime.php?limit=<limit>', this page groups all animes in order using rank information.
The command to use a crawl uses '<limit>' parameters to filter page visits.

```bash
$ scrapy runspider myanimelist/spiders/MyAnimeList.py \
  -a start_limit=<start_limit> \
  -a end_limit=<end_limit> \
```

#### MongoDB

The crawller result can be saved to mongodb by using the parameter "MONGODB_URL". This parameter indicates the connection URI as mongodb.

```bash
$ scrapy runspider myanimelist/spiders/MyAnimeList.py \
  -a start_limit=<start_limit> \
  -a end_limit=<end_limit> \
  -s MONGODB_URL=<mongo_uri>
```

## Dataset

This project create 3 datasets

### Animes

**animes.csv** contains list of anime, with title, title synonyms, genre, duration, rank, populatiry, score, airing date, episodes and many other important data about individual anime providing sufficient information about trends in time about important aspects of anime. Rank is in float format in csv, but it contains only integer value. This is due to NaN values and their representation in pandas.
```json
{
  "link": "https://myanimelist.net/anime/87/Mobile_Suit_Gundam__Chars_Counterattack",
  "uid": "87",
  "title": "Mobile Suit Gundam: Char's Counterattack",
  "synopsis": "The year is Universal Century 0093. Char Aznable has taken command of Neo Zeon, the rebels of outer space. He firmly believes that humankind can only achieve peace by relocating to space. Thus, he plans to crash the giant asteroid Axis into Earth and plunge the planet into an uninhabitable winter. Char also eagerly anticipates this opportunity to settle a 14-year rivalry with Amuro Ray. The two have been reluctant allies at times, but Char has never forgiven Amuro for causing the death of one of his comrades during the One Year War. \r\n \r\nOnly the Earth Federation's Londo Bell Unit has the power to stop Char from fulfilling his dangerous goal. Leading the defense of Earth is veteran captain Bright Noa and Amuro Ray with the latest Nu Gundam mobile suit. In this thrilling conclusion to the original Gundam series, Londo Bell engages in a final conflict with Neo Zeon that will decide the fate of Earth and end this long-standing rivalry—once and for all. \r\n \r\n[Written by MAL Rewrite]",
  "score": 7.73,
  "ranked": 1081,
  "popularity": 2604,
  "members": 29248,
  "genre": [
    "Military",
    "Sci-Fi",
    "Space",
    "Drama",
    "Mecha"
  ],
  "img_url": "https://cdn.myanimelist.net/images/anime/1523/92371.jpg",
  "episodes": "1",
  "aired": "Mar 12, 1988"
}
```

### Profiles

**profiles.csv** contains information about users who watch anime, namely username, birth date, gender, and favorite animes list.
```json
{
  "link": "https://myanimelist.net/profile/nyja-chan",
  "profile": "nyja-chan",
  "favorites": [
    "39195",
    "38000",
    "440",
    "457",
    "34599",
    "2251",
    "37779",
    "13125",
    "35180",
    "10721"
  ],
  "gender": "Female",
  "birthday": "Nov 13"
}
```

### Reviews

**reviews.csv** contains information about reviews users x animes, with text review and scores.
```json
{
  "link": "https://myanimelist.net/reviews.php?id=299323",
  "uid": "299323",
  "anime_uid": "1281",
  "profile": "Scarlet012",
  "text": "\n           \n         \n           \n             \n           \n         \n         \n           more pics \n         \n       \n         \n       \n         \n           Overall \n           9 \n         \n         \n           Story \n           7 \n         \n                   \n             Animation \n             8 \n           \n           \n             Sound \n             5 \n           \n                 \n           Character \n           10 \n         \n         \n           Enjoyment \n           9 \n         \n       \n     \n\n                    \n    This will be a review for the English dubbed version of the anime. (there may be spoilers!) \r\n \r\nBefore I get into the actual review, I'd like to just let it be known that the English dub and Japanese sub versions are different from one another. Because the original Japanese Gakkou no Kaiden did poorly, they gave it to an American studio to just \"do whatever they wanted\", and so they ended up making it much better, staying truer to the actual story, and even a little creepy. The English version was a funnier and less serious version of the original, and while though it has its serious moments they definitely aren't plentiful.  \r\n \r\nThe story was fairly enjoyable, I had a good time looking at all the different spirits and characters and how they had an impact on the story. Akane, as an example, was an interesting spirit. Her voice and her design both ended up complimenting each other, and her little \"flaw\" was played on really well. \r\n \r\nI loved the characters! This was, perhaps, the best part about this show. The characters were true to themselves (did not change personality randomly, or didn't feel like a different character at any point in the show). The characters were also hilariously funny, like Momoko's constant Christianity blurts, or Leo's being Jewish and constant knocks on that. The characters really made the show what it is, and made me wanting more. \r\n \r\nOverall, because of the story and the character development, I really enjoyed this show, and that's why I gave it a nine. There were some cringe-worthy parts, and other parts did not make sense, otherwise, this would be a straight ten!\n\n          \n \n       Helpful \n   \n      ",
  "scores": {
    "Overall": "9",
    "Story": "7",
    "Animation": "8",
    "Sound": "5",
    "Character": "10",
    "Enjoyment": "9"
  },
  "score": 9
}
```

## Kaggle 

This dataset is put on [Kaggle](https://www.kaggle.com/marlesson/myanimelist-dataset-animes-profiles-reviews)
