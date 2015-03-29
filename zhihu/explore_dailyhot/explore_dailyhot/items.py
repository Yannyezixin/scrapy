# -*- coding: utf-8 -*-

from scrapy import Item, Field

class ExploreDailyhotItem(Item):
    url = Field()
    title = Field()
    answer = Field()
