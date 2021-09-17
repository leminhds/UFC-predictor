import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import Selector
from fightcards.items import FightcardsItem


class CardsSpider(scrapy.Spider):
    name = 'cardsSpider'

    def start_requests(self):
        start_urls = [
            'http://ufcstats.com/statistics/events/completed?page=all'
        ]

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse_items)

    def parse_items(self, response):
        cardUrls = response.xpath("//td[@class='b-statistics__table-col']//i//a//@href").extract()
        for cardUrl in cardUrls:
            yield scrapy.Request(url=cardUrl, callback=self.parse_cards)

    def parse_cards(self, response):

        selector = Selector(response)
        fight_date = selector.xpath("//li[@class='b-list__box-list-item']/text()").extract()[1]
        fights_location = selector.xpath("//li[@class='b-list__box-list-item']/text()").extract()[3]

        for td in selector.xpath('//tbody[@class="b-fight-details__table-body"]//tr'):
            item = FightcardsItem()
            item['fight_date'] = fight_date
            item['fights_location'] = fights_location
            item['f1'] = td.xpath('td[2]//a//text()').extract()[0]
            item['f2'] = td.xpath('td[2]//a//text()').extract()[1]
            item['weight_class'] = td.xpath('td[7]//p/text()').extract_first()
            item['winning_method'] = td.xpath('td[8]//p/text()').extract_first()
            # first name are always the winner
            item['winner'] = item['f1']

            fight_url = td.xpath('@data-link').extract()[0]

            yield scrapy.Request(url=fight_url, callback=self.parse_fights, meta={'card_item': item})

    def parse_fights(self, response):
        item = response.meta.get('card_item')
        item['card_name'] = response.xpath("//h2[@class='b-content__title']//a//text()").extract_first()
        item['round_fought'] = response.xpath("//i[@class='b-fight-details__text-item'][1]//text()").extract()[2]
        item['round_format'] = response.xpath("//i[@class='b-fight-details__text-item'][3]//text()").extract()[2]

        for td in response.xpath('//section[@class="b-fight-details__section js-fight-section"][2]//table//tbody//tr'):
            item['f1_sig_strike_total'] = td.xpath('td[3]//p[1]//text()').extract_first()
            item['f1_sig_strike_per'] = td.xpath('td[4]//p[1]//text()').extract_first()
            item['f2_sig_strike_total'] = td.xpath('td[3]//p[2]//text()').extract_first()
            item['f2_sig_strike_per'] = td.xpath('td[4]//p[2]//text()').extract_first()
            item['f1_td_attempt'] = td.xpath('td[6]//p[1]//text()').extract_first()
            item['f2_td_attempt'] = td.xpath('td[6]//p[2]//text()').extract_first()
            item['f1_td_succeed'] = td.xpath('td[6]//p[1]//text()').extract_first()
            item['f2_td_succeed'] = td.xpath('td[6]//p[2]//text()').extract_first()

        return item
