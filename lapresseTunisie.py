#This command installs the Scrapy framework via pip.
!pip install Scrapy

# This command initializes a new Scrapy project named "lapresseTunisie", which will be used for web scraping tasks related to "La Presse Tunisie".
!scrapy startproject lapresseTunisie

# This command changes the current directory to the "spiders" directory within the "lapresseTunisie" project, allowing for easy access to the Python scripts responsible for crawling and scraping specific website pages.
%cd lapresseTunisie/lapresseTunisie/spiders

# This command generates a new spider named "presseTunisie" for the website "https://lapresse.tn/" within the Scrapy project. The spider will be used to define the scraping logic for extracting data from the specified website.
!scrapy genspider presseTunisie https://lapresse.tn/

# This code defines a Scrapy spider named "lapresseTunisie" designed to scrape data from the website "https://lapresse.tn/".
# The spider extracts information such as the 'title', 'description', and 'date' from news articles on the website.
%%writefile lapresseTunisie.py
import scrapy
class PressetunisieSpider(scrapy.Spider):
    name = "lapresseTunisie"
    allowed_domains = ["lapresse.tn"]
    start_urls = ["https://lapresse.tn/"]
    def parse(self, response):
        news=response.css('div.bdaia-block-wrap')
        for n in news:
          yield{
            'title':n.css('div header h2 a span::text').get(),
            'description':n.css('div p::text').get(),
            'date':n.css('footer div span::text').get(),
          }

# This command instructs Scrapy to execute the spider named "lapresseTunisie" and save the scraped data into a JSON file named "news_data.json".
!scrapy crawl lapresseTunisie -o news_data.json

# This code imports the json module to work with JSON data.
# It opens the 'news_data.json' file in read mode and loads its contents into the variable 'data' using the json.load() function.
# Finally, it prints the length of the data, which typically represents the number of items or records extracted from the JSON file.
import json
with open('news_data.json', 'r') as file:
   data = json.load(file)
print(len(data))

# This code retrieves the first item from the 'data' list and assigns it to the variable 'first_news'.
# It then prints the title, date, and description of the first news item extracted from the JSON data.
first_news=data[0]
print(f"Title: {first_news['title']}")
print(f"Date: {first_news['date']}")
print(f"News_content: {first_news['description']}")


