# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    detail_url = scrapy.Field()
    title = scrapy.Field()
    salary = scrapy.Field()
    contract_type = scrapy.Field()
    job_type = scrapy.Field()
    location = scrapy.Field()
