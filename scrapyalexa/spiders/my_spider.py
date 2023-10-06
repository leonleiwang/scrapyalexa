import scrapy
from scrapy.http import Request
from scrapyalexa.items import ScrapyalexaItem
from bs4 import BeautifulSoup
import re
import time
from scrapyalexa import settings  # Import project settings

class MySpider(scrapy.Spider):
    name = "scrapyalexa"

    def start_requests(self):
        for region, url in settings.BASE_URLS.items():
            yield Request(url=url, callback=self.parse_asin, meta={'region': region})

        for region, url in settings.ALEXA_STORE_URLS.items():
            yield Request(url=url, callback=self.parse_skill, meta={'region': region})

    def parse_asin(self, response):
        region = response.meta.get('region')
        asin_list = self.extract_asin(response)
        for asin in asin_list:
            item = ScrapyalexaItem()
            item['region'] = region
            item['asin'] = asin
            yield item

    def parse_skill(self, response):
        region = response.meta.get('region')
        skill_list = self.extract_skill(response)
        for skill in skill_list:
            item = ScrapyalexaItem()
            item['region'] = region
            item['skill'] = skill
            yield item

    def extract_asin(self, response):
        # Your ASIN extraction logic
        pass

    def extract_skill(self, response):
        # Your skill extraction logic
        pass