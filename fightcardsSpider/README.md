# Scraping UFC fighters statistic

This spider go through the website http://www.ufcstats.com/statistics/events/completed and scrape out specific match statistic of the matches in different events 


## Getting started

If you want to scrape again from scratch to get the latest fighters' data, 

First, make sure you have scrapy (I would recommend that you create a separate environment before running the following command):
```bash
pip isntall scrapy
```


after Cloning the project, cd to fightcardsSpider/fightcards/spiders. Then, from the Command Lines, run:

```bash
scrapy runspider cardsSpider.py
```

or if you want to generate a csv file directly after scraping, run the following command, it will create a csv file with the name "fighters.csv" in the same folder:
```bash
scrapy runspider cardsSpider.py -o fighters.csv -t csv
```

and that's it!

## Items collected
The following items are collected:
```python
    card_name = Field()
    fight_date = Field()
    fights_location = Field()
    round_format = Field()
    round_fought = Field()
    winner = Field()
    winning_method = Field()
    weight_class = Field()
    f1 = Field()
    f2 = Field()
    f1_sig_strike_total = Field()
    f2_sig_strike_total = Field()
    f1_sig_strike_per = Field()
    f2_sig_strike_per = Field()
    f1_td_attempt = Field()
    f2_td_attempt = Field()
    f1_td_succeed = Field()
    f2_td_succeed = Field()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
