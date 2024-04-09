import scrapy
import csv


class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.softwareadvice.com/categories/']
    output_file = 'output.csv'
    parsed_data = set()

    def parse(self, response):
        # Extract href attributes from a tags with specified class
        a_tags = response.css('a.mr-2.font-bold.text-spacecadet-600.no-underline.hover\\:underline')
        for a_tag in a_tags:
            href = a_tag.css('::attr(href)').get()
            if href:
                href_with_path = href + "p/all/"
                yield response.follow(href_with_path, callback=self.parse_category_page)

    def parse_category_page(self, response):
        # Extract text enclosed within h3 tags under a tags
        h3_tags = response.css('a h3::text').getall()
        for text in h3_tags:
            self.parsed_data.add(text.strip())

    def closed(self, reason):
        # Write extracted text to CSV file
        with open(self.output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['product']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in self.parsed_data:
                writer.writerow({'product': item})


# Run the spider
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess()
process.crawl(MySpider)
process.start()
