# -*- coding: utf-8 -*-
import scrapy

from douban_movie_top_250.items import DoubanMovieTop250Item


class Top250Spider(scrapy.Spider):
    name = "top250"
    allowed_domains = ["movie.douban.com"]
    start_urls = (
        'http://movie.douban.com/top250?start={page}',
    )

    def start_requests(self):
        urls = []
        start_urls = self.start_urls[0]
        for i in range(10):
            urls.append(start_urls.format(page = str(25 * i)))

        for url in urls:
            yield scrapy.FormRequest(url, callback = self.parse)

    def parse(self, response):
        item = DoubanMovieTop250Item()
        containers = response.xpath('//div[contains(@class, "hd")]/a')
        for name in containers:
            item['name'] = name.xpath('span/text()')[0].extract()
            yield item
