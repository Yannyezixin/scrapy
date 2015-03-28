# -*- coding: utf-8 -*-
BOT_NAME = 'douban_movie_top_250'

SPIDER_MODULES = ['douban_movie_top_250.spiders']
NEWSPIDER_MODULE = 'douban_movie_top_250.spiders'

ITEM_PIPELINES = {
    'douban_movie_top_250.pipelines.JsonWriterPipeline': 200
}

