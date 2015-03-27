# -*- coding: utf-8 -*-

# Scrapy settings for qiushibaike project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'qiushibaike'

SPIDER_MODULES = ['qiushibaike.spiders']
NEWSPIDER_MODULE = 'qiushibaike.spiders'

ITEM_PIPELINES = {
    'scrapy.contrib.pipeline.images.ImagesPipeline': 1,
    'qiushibaike.pipelines.QiushiImagePipeline': 100,
}
IMAGES_STORE = './images-hot'

HEADER = {
    'Host': 'www.qiushibaike.com',
    'Referer': 'http://www.qiushibaike.com/hot',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'qiushibaike (+http://www.yourdomain.com)'
