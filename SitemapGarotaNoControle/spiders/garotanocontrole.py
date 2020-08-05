# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector



class GarotanocontroleSpider(scrapy.Spider):
    name = 'garotanocontrole'
    allowed_domains = ['https://garotanocontrole.com.br/']
    start_urls = ['https://garotanocontrole.com.br/']
    #sitemap_rules = [('trump', 'parse_article')]

    #def parse_article(self, response):
    #    print('parse_article url:', response.url)
         

    def parse(self, response):
        slides = response.css('.slider-featured-image')
        for s in slides:
            selector = Selector(text=s.get())
            yield {
                'type':'slides',
                'url' : selector.xpath('//a/@href').get(),
                'title' :  selector.xpath('//a/@title').get(),
                'url_img' : selector.xpath('//img/@src').get()
            }
        sections = response.css('.single-article')
        print(len(sections))
        for s in sections:
            selector = Selector(text=s.get())
            category = Selector(text=selector.css('.cat-links').get())
            yield {
                'type':'topics',
                'category' : category.xpath('//a/text()').get(),
                'url' :  selector.xpath('//a/@href').get(),
                'title' :  selector.xpath('//a/@title').get(),
                'url_img' : selector.xpath('//img/@src').get()
            }
       