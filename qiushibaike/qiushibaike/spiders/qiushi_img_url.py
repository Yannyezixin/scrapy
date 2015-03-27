# -*- coding: utf-8 -*-
import scrapy

from qiushibaike.settings import *
from qiushibaike.items import QiushibaikeItem


class HotImageSpider(scrapy.Spider):
    name = "hot-image"
    allowed_domains = ["www.qiushibaike.com"]
    start_urls = (
        'http://www.qiushibaike.com/hot/page/',
    )

    def __init__(self):
        self.headers = HEADER

    def start_requests(self):
        urls = []
        for i in range(1, 150):
            urls.append(self.start_urls[0] + str(i))

        for idx, url in enumerate(urls):
            yield scrapy.FormRequest(url, \
                                     headers = self.headers, \
                                     callback = self.parse_item)

    def parse_item(self, response):
        item = QiushibaikeItem()
        containers = response.xpath('//div[contains(@class, "thumb")]')
        for container in containers:
            item['image_urls'] = container.xpath('a/img/@src').extract()
            yield item
