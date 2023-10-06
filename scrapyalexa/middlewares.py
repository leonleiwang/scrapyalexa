from scrapy import signals
from fake_useragent import UserAgent
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class RandomUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent=""):
        super().__init__(user_agent)
        self.ua = UserAgent()

    def process_request(self, request, spider):
        user_agent = self.ua.random
        if user_agent:
            request.headers.setdefault('User-Agent', user_agent)

class ScrapyAlexaDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)