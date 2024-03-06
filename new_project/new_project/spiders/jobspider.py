import scrapy
from new_project.items import NewProjectItem


class JobspiderSpider(scrapy.Spider):
    name = "jobspider"
    page_number = 2
    allowed_domains = ["www.reed.co.uk"]
    start_urls = ["https://www.reed.co.uk/jobs/data-analyst-jobs"]

    def parse(self, response):
       job_item = NewProjectItem()
       joblist = response.xpath('//header')
       for sel in joblist:
            job_item['detail_url'] = sel.xpath('h2/a/@href').extract()
            job_item['title'] = sel.xpath('h2/a/text()').extract()
            job_item['salary'] = sel.xpath('ul/li[1]/text()').extract()
            joblist_type = sel.xpath('ul/li[3]/text()').extract()
            final_type = ', '.join(joblist_type)
            joblist_types = list(final_type.split(', '))
            job_item['contract_type'] = joblist_types[::2]
            job_item['job_type'] = joblist_types[1::2]
            job_item['location'] = sel.xpath('ul/li[2]/text()').extract()

            yield job_item
       
       next_page = 'https://www.reed.co.uk/jobs/data-analyst-jobs?pageno=' + str(JobspiderSpider.page_number)
       if JobspiderSpider.page_number <= 119:
            JobspiderSpider.page_number += 1
            yield response.follow(next_page, callback= self.parse)


        
