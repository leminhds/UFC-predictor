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
    DoB = Field()  # date of birth
    SLpM = Field()  # strike landed per
    strAcc = Field()  # strike accuracy in percentage
    SApM = Field()  # strike absorbed per
    strDef = Field()  # strikes defence
    tdAvg = Field()  # takedown average
    tdAcc = Field()  # take down accuracy/success in percentage
    tdDef = Field()  # take down defense
    subAvg = Field()  # submission average