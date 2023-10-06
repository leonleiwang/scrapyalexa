import pymongo
from scrapy.exceptions import DropItem
from scrapyalexa.settings import MONGODB_URI, MONGODB_DATABASE
from .items import ScrapyalexaItem

class ScrapyAlexaPipeline:
    def __init__(self):
        self.client = pymongo.MongoClient(MONGODB_URI)
        self.db = self.client[MONGODB_DATABASE]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem(f"Missing {data}!")
        if valid:
            # Specify the collection based on the spider name
            collection_name = spider.name
            collection = self.db[collection_name]
            collection.insert_one(dict(item))
            return item