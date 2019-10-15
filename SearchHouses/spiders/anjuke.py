# -*- coding: utf-8 -*-
import scrapy
from SearchHouses.items import SearchhousesItem
from datetime import date


class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'
    allowed_domains = ['wh.fang.anjuke.com']
    start_urls = ['https://wh.fang.anjuke.com/loupan/all/p1/']

    def parse(self, response):
        # print(response.url)

        url_list = response.xpath(
            '//div[@class="key-list imglazyload"]/div[@class="item-mod "]')
        for url_li in url_list:
            url = url_li.xpath('./@data-link').extract_first()
            area = url_li.xpath(
                './/a[@class="huxing"]/span[last()]/text()').extract_first()     
            yield scrapy.Request(
                url=url, 
                callback=self.parse_detail, 
                meta={
                    'area': area, 
                    'today': date.today().strftime('%Y%m%d')
                    }
                )
        
        next_url = response.xpath(
            '//a[@class="next-page next-link"]/@href').extract_first()
        if next_url is not None:
            yield scrapy.Request(
                url=next_url, 
                callback=self.parse, 
                dont_filter=True
                )

    def parse_detail(self, response):
        item = SearchhousesItem()
        item['collection'] = 'anjuke_newhouse_{}'.format(
            response.meta.get('today', '')
            )
        item['url'] = response.url
        item['area'] = response.meta.get('area', None)
        
        basic_info = response.xpath(
            '//div[@class="basic-info"]')[0]
        item['lp_name'] = basic_info.xpath(
            './h1/text()').extract_first()
        item['lp_alias'] = basic_info.xpath(
            './p/text()').extract_first()

        basic_params = response.xpath('//dl[@class="basic-parms clearfix"]')[0]
        item['price'] = basic_params.xpath('./dd[@class="price"]//text()').extract()
        item['huxing'] = basic_params.xpath('.//div[@class="house-item g-overflow"]//a/text()').extract()
        item['address'] = basic_params.xpath('.//a[@class="lpAddr-text g-overflow"]/text()').extract_first()
        yield item

