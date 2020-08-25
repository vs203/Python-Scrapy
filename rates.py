# -*- coding: utf-8 -*-
import scrapy
from ..items import LiveRatesItem
class RatesSpider(scrapy.Spider):
    name = 'rates'
    start_urls = ['https://economictimes.indiatimes.com/markets/forex']

    def parse(self, response):

            items = LiveRatesItem()
            Description = response.css('.alignC a::text').extract()
            rate = response.css('.price').css('::text').extract()
            previous_close = response.css('.fRatesData .alignR:nth-child(6)').css('::text').extract()
            items['Description'] = Description
            items['Rate'] = rate
            items['Previous_Close'] = previous_close

            yield items


