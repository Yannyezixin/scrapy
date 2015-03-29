# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest
from scrapy.contrib.linkextractors import LinkExtractor
from explore_dailyhot.items import ExploreDailyhotItem
from explore_dailyhot.settings import *


class DailyhotSpider(CrawlSpider):
    name = "dailyhot"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['http://www.zhihu.com/explore']
    """
    rules = (
        Rule(LinkExtractor(allow=('/question/\d+/answer/\d+', )), callback = 'parse_page', follow = True),
    )
    """

    def start_requests(self):
        return [FormRequest("http://www.zhihu.com/login", \
                            meta = {'cookiejar': 1}, \
                            callback = self.post_login)]

    def post_login(self, response):
        print "准备登陆"
        _xsrf = response.xpath('//input[contains(@name, "_xsrf")]/@value').extract()[0]
        print _xsrf
        return [FormRequest.from_response(response,
                    meta = {'cookiejar': response.meta['cookiejar']},
                    headers = HEADER,
                    formdata = {
                        '_xsrf': _xsrf,
                        'email': 'youremail',
                        'password': '123466',
                        'rememberme': 'y'
                    },
                    callback = self.after_login,
                    dont_filter = True
                    )]

    def after_login(self, response):
        print "after_login"
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        item = ExploreDailyhotItem()
        questions = response.xpath('//div[@data-type="daily"]/div')
        for question in questions:
            item['url'] = question.xpath('h2/a/@href').extract()
            item['title'] = question.xpath('h2/a/text()').extract()
            item['answer'] = question.xpath('div/div/textarea[@class="content hidden"]/text()').extract()
            yield item

