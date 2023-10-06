from scrapy import cmdline

# Replace 'scrapyalexa' with the actual spider name you defined in your Scrapy project
spider_name = 'scrapyalexa'

cmd = f"scrapy crawl {spider_name}"
cmdline.execute(cmd.split())