# Scraping UFC fighters statistic

This spider go through the website http://www.ufcstats.com/statistics/fighters to scrape out the detailed data of each fighter in the UFC

## Getting started

If you want to scrape again from scratch to get the latest fighters' data, 

First, make sure you have scrapy (I would recommend that you create a separate environment before running the following command):
```bash
pip isntall scrapy
```


after Cloning the project, cd to fighterSpider/fighterSpider/spiders. Then, from the Command Lines, run:

```bash
scrapy runspider fightersSpider.py
```

or if you want to generate a csv file directly after scraping, run the following command, it will create a csv file with the name "fighters.csv" in the same folder:
```bash
scrapy runspider fightersSpider.py -o fighters.csv -t csv
```

and that's it!

## Items collected
```python
name = Field()
record = Field()
height = Field()
weight = Field()
reach = Field()
stance = Field()
DoB = Field() # date of birth
SLpM = Field() # strike landed per 
strAcc = Field() # strike accuracy in percentage
SApM = Field() # strike absorbed per 
strDef = Field() # strikes defence
tdAvg = Field() # takedown average
tdAcc = Field() # take down accuracy/success in percentage
tdDef = Field() # take down defense
subAvg = Field() # submission average
```


## Challenges
Despite the fact that the data seem to be normalized, the data format varies greatly, depending on the time the fight took place. Some data, such as fighter stance, reach, height could be missing as well. 

The missing data here come with its own set of challenges. Not all missing data are marked the same way.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
