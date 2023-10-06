# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyalexaItem(scrapy.Item):
    # Define your item fields here
    region = scrapy.Field()
    asin = scrapy.Field()
    skill = scrapy.Field()