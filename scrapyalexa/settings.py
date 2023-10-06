import os

BOT_NAME = 'scrapyalexa'

SPIDER_MODULES = ['scrapyalexa.spiders']
NEWSPIDER_MODULE = 'scrapyalexa.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'

ROBOTSTXT_OBEY = True

# Maximum concurrent requests
CONCURRENT_REQUESTS = 5

# Retrying failed requests (Scrapy automatically retries 2 times by default)
RETRY_TIMES = 5

DOWNLOAD_DELAY = 0.5
# API_KEY = "YO39P22MOYUWZCUTA7OEDA2GZ5LAVQA74WQKTIKOOEDQSBLRB6Z8H9YW52V13MTT7X9ZVWAYOUGDQXKH"

MONGODB_URI = "mongodb://localhost:27017"
# MONGODB_DATABASE = "alexacrawler_test"
MONGODB_DATABASE = "scrapyalexa"

# Downloader Middleware
# Enable User Agent middleware
# Enable Proxy Middleware
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapyalexa.middlewares.RandomUserAgentMiddleware': 400, # 使用你自己的中间件
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,
}

# def parse(self, response):
#     request = scrapy.Request("http://www.example.com/some_page.html")
#     request.meta['proxy'] = "http://YOUR_PROXY_IP:PORT"
#     yield request

BASE_URLS = {
    'US': 'https://www.amazon.com/',
    'AU': 'https://www.amazon.com.au/',
    'UK': 'https://www.amazon.co.uk/',
    'BR': 'https://www.amazon.com.br/',
    'CA': 'https://www.amazon.ca/',
    'FR': 'https://www.amazon.fr/',
    'DE': 'https://www.amazon.de/',  # germany
    'IN': 'https://www.amazon.in/',
    'IT': 'https://www.amazon.it/',
    'JP': 'https://www.amazon.co.jp/',
    'MX': 'https://www.amazon.com.mx/',
    'ES': 'https://www.amazon.es/'  # spain
}

ALEXA_STORE_URLS = {
    'US': 'https://www.amazon.com/s?i=alexa-skills&bbn=13727921011',
    'AU': 'https://www.amazon.com.au/b?ie=UTF8&node=4931595051',
    'UK': 'https://www.amazon.co.uk/s?i=alexa-skills',
    'BR': 'https://www.amazon.com.br/b?ie=UTF8&node=17938238011',
    'CA': 'https://www.amazon.ca/b?ie=UTF8&node=16286269011',
    'FR': 'https://www.amazon.fr/b?ie=UTF8&node=13944548031',
    'DE': 'https://www.amazon.de/b?ie=UTF8&node=10068460031',
    'IN': 'https://www.amazon.in/b?ie=UTF8&node=11928183031',
    'IT': 'https://www.amazon.it/b?ie=UTF8&node=13944605031',
    'JP': 'https://www.amazon.co.jp/b?ie=UTF8&node=4788676051',
    'MX': 'https://www.amazon.com.mx/b?ie=UTF8&node=17553254011',
    'ES': 'https://www.amazon.es/b?ie=UTF8&node=13944662031'
}

BASE_PATH = os.path.expanduser("~/scrapyalexa_downloads/")
SETTINGS_FILES_PATH = 'setting_files/'
# BASE_PATH = 'D:\\crawler\\scrapy\\ScrapyCrawler\\alexacrawler_downloads\\'
# SETTINGS_FILES_PATH = 'D:\\crawler\\scrapy\\ScrapyCrawler\\setting_files\\'

DEP_PATH = SETTINGS_FILES_PATH + '/dep/'
DEP_PNUM_PATH = SETTINGS_FILES_PATH + 'dep_pnum/'
RAW_PATH = BASE_PATH + 'raw/'
DEBUG_FILES_PATH = BASE_PATH + 'debug_files/'

# Enables or disables scraping pages in a random order
RANDOMIZE_DOWNLOAD_DELAY = True

GET_ALL_ASIN_PROGRESS_FILE_PATH = SETTINGS_FILES_PATH