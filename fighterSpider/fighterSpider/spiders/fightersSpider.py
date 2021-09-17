import scrapy

from scrapy import Selector
from scrapy.crawler import CrawlerProcess

from fighterSpider.items import FighterspiderItem

import string

class Fighters(scrapy.Spider):
    name = "fighterSpider"

    def start_requests(self):
        start_urls = [
            # the names are spread across multiple pages by alphabet order
            'http://ufcstats.com/statistics/fighters?char=' + letter + '&page=all' for letter in string.ascii_lowercase
        ]

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse_items)


    def parse_items(self, response):
        links = response.xpath("//td[@class = 'b-statistics__table-col']//@href").extract()
        links = set(links)
        for link in links:
            yield scrapy.Request(link, callback=self.parse_fighter)


    def parse_fighter(self, response):
        selector = Selector(response)
        item = FighterspiderItem()
        item['name'] = selector.xpath("//span[@class='b-content__title-highlight']//text()").extract_first()
        item['record'] = selector.xpath("//span[@class='b-content__title-record']//text()").extract_first()


        for stat in response.xpath('//ul[@class="b-list__box-list"]'):

            item['DoB'] = stat.xpath('li[5]//text()').extract()[2]


            # for the items below, for the earliest fights
            # in ufc history, the data are often missing
            try:
                item['height'] = stat.xpath('li[1]//text()').extract()[2]
            except:
                item['height'] = None

            try:
                item['weight'] = stat.xpath('li[2]//text()').extract()[2]
            except:
                item['weight'] = None

            try:
                if stat.xpath('li[3]//text()').extract()[2] == "\n      --\n    " or \
                        stat.xpath('li[3]//text()').extract()[2] == "\n      \n    ":
                    item['reach'] = None
                else:
                    item['reach'] = stat.xpath('li[3]//text()').extract()[2]
            except:
                item['reach'] = None


            try:
                if stat.xpath('li[4]//text()').extract()[2] =="\n      --\n    " or \
                        stat.xpath('li[4]//text()').extract()[2] =="\n      \n    ":
                    item['stance'] = None
                else:
                    item['stance'] = stat.xpath('li[4]//text()').extract()[2]
            except:
                item['stance'] = None

        for stat in response.xpath('//div[@class="b-list__info-box-left"]//ul'):
            item['SLpM'] = stat.xpath('li[1]//text()').extract()[2]
            item['strAcc'] = stat.xpath('li[2]//text()').extract()[2]
            item['SApM'] = stat.xpath('li[3]//text()').extract()[2]
            item['strDef'] = stat.xpath('li[4]//text()').extract()[2]

        for stat in response.xpath('//div[@class="b-list__info-box-right b-list__info-box_style-margin-right"]//ul'):
            item['tdAvg'] = stat.xpath('li[2]//text()').extract()[2]
            item['tdAcc'] = stat.xpath('li[3]//text()').extract()[2]
            item['tdDef'] = stat.xpath('li[4]//text()').extract()[2]
            item['subAvg'] = stat.xpath('li[5]//text()').extract()[2]

        return item