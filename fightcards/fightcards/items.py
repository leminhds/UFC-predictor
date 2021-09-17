# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class FightcardsItem(Item):
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



