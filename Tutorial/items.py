# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ColumItem(scrapy.Item):
	# class_timing = scrapy.Field()
	# day = scrapy.Field()
	# desc = scrapy.Field()
	# teacher = scrapy.Field()
	title = scrapy.Field()
	timing = scrapy.Field()
	date = scrapy.Field()