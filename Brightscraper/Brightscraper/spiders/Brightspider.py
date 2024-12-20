import scrapy


class BrightspiderSpider(scrapy.Spider):
    name = "Brightspider"
    allowed_domains = ["brightscholarship.com"]
    start_urls = ["http://brightscholarship.com/"]

    def parse(self, response):
        pass
