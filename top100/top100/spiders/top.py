# -*- coding: utf-8 -*-
import scrapy
from top100.items import Top100Item
from urllib import parse
from scrapy.http import Request
class TopSpider(scrapy.Spider):
    name = 'top'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/board/4?offset=%s'%i for i in range(0,100,10) ]

    def parse(self, response):
        # item = Top100Item()
        # name = response.css('.name a::text').extract()
        # time = response.css('.releasetime::text').extract()
        # cart = response.css('.star::text').extract()
        # front_image_url = response.css('.image-link .board-img::attr(data-src)').extract()
        artcle_url = response.css('.name a::attr(href)').extract()
        
        # item['name']=name
        # item['time']=time
        # item['cart']=cart
        # item['front_image_url']=[front_image_url]
        # yield item
        # for i in artcle_url:
        #     url = 'http://maoyan.com%s'%(i)
        yield Request(url=parse.urljoin(response.url,artcle_url),callback=self.contentparse)
    def contentparse(self,response):
        print(response.url)


