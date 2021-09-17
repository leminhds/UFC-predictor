# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class FighterspiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    record = Field()
    height = Field()
    weight = Field()
    reach = Field()
    stance = Field()
    DoB = Field()
    SLpM = Field()
    strAcc = Field()
    SApM = Field()
    strDef = Field()
    tdAvg = Field()
    tdAcc = Field()
    tdDef = Field()
    subAvg = Field()