# This command installs the Scrapy framework via pip.
!pip install scrapy

# This command initializes a new Scrapy project named "nbcNews", providing a framework for web scraping tasks related to NBC News.
!scrapy startproject nbcNews

# This command changes the current directory to the "spiders" directory within the "nbcNews" project. It facilitates access to the Python scripts responsible for crawling and scraping specific pages of the NBC News website.
%cd nbcNews/nbcNews/spiders

# This command generates a new spider named "nbcNew" for the website "https://www.nbcnews.com" within the Scrapy project. The spider will be used to define the scraping logic for extracting data from the specified NBC News website.
!scrapy genspider nbcNew https://www.nbcnews.com

# This code defines a Scrapy spider named "nbcNews" intended for scraping data from the website "https://www.nbcnews.com".
# The spider is programmed to extract information such as the 'title', 'description', and 'date' from news articles on the NBC News website.
%%writefile nbcNews.py
import scrapy
class NbcnewSpider(scrapy.Spider):
    name = "nbcNews"
    allowed_domains = ["www.nbcnews.com"]
    start_urls = ["https://www.nbcnews.com"]
    def parse(self, response):
        news=response.css('div div.styles_wrapper__rLlka')
        for n in news:
          yield{
            'title':n.css('div h2 a::text').get(),
            'description': n.css('div div::text').get(),
            'date': n.css(' div div::text').get(),
          }

# This command instructs Scrapy to execute the spider named "nbcNews" and save the scraped data into a JSON file named "news_data.json".
!scrapy crawl nbcNews -o news_data.json

# This code imports the json module to handle JSON data.
# It opens the 'news_data.json' file in read mode and loads its contents into the variable 'data' using json.load().
# Finally, it prints the length of the data, indicating the number of items extracted from the JSON file.
import json
with open('news_data.json', 'r') as file:
   data = json.load(file)
print(len(data))

# This code retrieves the first item from the 'data' list and assigns it to the variable 'first_news'.
# Then, it prints the title, date, and news content of the first news item extracted from the JSON data.
first_news=data[0]
print(f"Title: {first_news['title']}")
print(f"Date: {first_news['date']}")
print(f"News_content: {first_news['description']}")
