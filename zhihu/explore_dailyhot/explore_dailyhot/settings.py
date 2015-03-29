# -*- coding: utf-8 -*-

BOT_NAME = 'explore_dailyhot'

SPIDER_MODULES = ['explore_dailyhot.spiders']
NEWSPIDER_MODULE = 'explore_dailyhot.spiders'

ITEM_PIPELINES = {
    'explore_dailyhot.pipelines.JsonWriterPipeline': 100
}

HEADER = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
    "Connection": "keep-alive",
    "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
    'Host': 'www.zhihu.com',
    'Referer': 'http://www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36',
}

DOWNLOAD_DELAY = 0.25
