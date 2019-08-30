# -*- coding: utf-8 -*-
import scrapy


class SubjectsSpider(scrapy.Spider):
    name = 'subjects'
    allowed_domains = ['classcentral.com']
    start_urls = ['http://classcentral.com/']

    def parse(self, response):
        pass
