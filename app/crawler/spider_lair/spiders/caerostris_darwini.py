"""Caerostris Darwini Spiders.

Categories:
+ Commentarial (image/text)
+ Commercial (image)
+ Encyclopedic (text)
+ Videographic (video)
"""

import scrapy
from scrapy import signals

# class CDCommentarial(scrapy.Spider):
#     """Commentarial spider."""

#     name = 'caerostris_darwini_commentarial'
#     start_urls = ['https://bbc.com/', 'https://espn.com/', 'https://ign.com/']
#     COUNT_MAX = 5
#     count = 0

#     def parse(self, response):
#         """Follow links."""
#         yield from response.follow_all(css='a::attr(href)', callback=self.parse_data)
        
        
#     def parse_data(self, response):
#         """Process data from followed links."""
#         try:
    #         all_text = response.css('*:not(script):not(style)::text')
#             for text in all_text:
#                 print(response)
#                 if self.query in text.get():
#                     yield { 'url': response.request.url, 'text': text.get() }
#                     # CloseSpider()
#         except:
#             print('End of the line error.')

# class CDEncyclopedic(scrapy.Spider):
#     """Encyclopedic spider."""

#     name = 'caerostris_darwini_encyclopedic'
#     start_urls = ['https://en.m.wikipedia.org/', 'https://nih.gov/', 'https://thebulletin.org/']
#     COUNT_MAX = 5
#     count = 0

#     def parse(self, response):
#         """Follow links."""
#         yield from response.follow_all(css='a::attr(href)', callback=self.parse_data)
        
#     def parse_data(self, response):
#         """Process data from followed links."""
#         try:
    #         all_text = response.css('*:not(script):not(style)::text')
#             for text in all_text:
#                 if self.query in text.get():
#                     yield { 'url': response.request.url, 'text': text.get() }
#                     # CloseSpider()
#         except:
#             print('End of the line error.')

# class CDBroadCrawler(scrapy.Spider):
#     """Broad crawling spider."""

#     name = 'caerostris_darwini_broad_crawler'
#     start_urls = ['https://en.m.wikipedia.org/']
#     COUNT_MAX = 5
#     count = 0

#     def parse(self, response):
#         """Follow links."""
#         link_frontier = response.css('a::attr(href)')
#         # print('frontier', link_frontier)
#         for link in link_frontier:
#             print('curr link', link)
#             yield response.follow(link, callback=self.parse)

#         all_text = response.css('*:not(script):not(style)::text')
#         for text in all_text:
#             if self.query in text.get():
#                 yield { 'url': response.request.url, 'text': text.get() }
#                 print({ 'url': response.request.url })

class BroadCrawler1(scrapy.Spider):
    """Broad crawling spider."""

    name = 'broad_crawler_1'
    start_urls = ['https://en.m.wikipedia.org/']

    def parse(self, response):
        """Follow links."""
        try:
            all_text = response.css('*:not(script):not(style)::text')
            for text in all_text:
                if self.query in text.get(): yield { 'url': response.request.url, 'text': text.get() }
        except: print(f'End of the line error for {self.name}.')

        yield from response.follow_all(css='a::attr(href)', callback=self.parse)

class BroadCrawler2(scrapy.Spider):
    """Broad crawling spider."""

    name = 'broad_crawler_2'
    start_urls = ['https://nih.gov/']

    def parse(self, response):
        """Follow links."""
        try:
            all_text = response.css('*:not(script):not(style)::text')
            for text in all_text:
                if self.query in text.get(): yield { 'url': response.request.url, 'text': text.get() }
        except: print(f'End of the line error for {self.name}.')

        yield from response.follow_all(css='a::attr(href)', callback=self.parse)

class BroadCrawler3(scrapy.Spider):
    """Broad crawling spider."""

    name = 'broad_crawler_3'
    start_urls = ['https://thebulletin.org/']

    def parse(self, response):
        """Follow links."""
        try:
            all_text = response.css('*:not(script):not(style)::text')
            for text in all_text:
                if self.query in text.get(): yield { 'url': response.request.url, 'text': text.get() }
        except: print(f'End of the line error for {self.name}.')

        yield from response.follow_all(css='a::attr(href)', callback=self.parse)

class BroadCrawler4(scrapy.Spider):
    """Broad crawling spider."""

    name = 'broad_crawler_4'
    start_urls = ['https://bbc.com/']

    def parse(self, response):
        """Follow links."""
        try:
            all_text = response.css('*:not(script):not(style)::text')
            for text in all_text:
                if self.query in text.get(): yield { 'url': response.request.url, 'text': text.get() }
        except: print(f'End of the line error for {self.name}.')

        yield from response.follow_all(css='a::attr(href)', callback=self.parse)

class BroadCrawler5(scrapy.Spider):
    """Broad crawling spider."""

    name = 'broad_crawler_5'
    start_urls = ['https://espn.com/']

    def parse(self, response):
        """Follow links."""
        try:
            all_text = response.css('*:not(script):not(style)::text')
            for text in all_text:
                if self.query in text.get(): yield { 'url': response.request.url, 'text': text.get() }
        except: print(f'End of the line error for {self.name}.')

        yield from response.follow_all(css='a::attr(href)', callback=self.parse)

class BroadCrawler6(scrapy.Spider):
    """Broad crawling spider."""

    name = 'broad_crawler_6'
    start_urls = ['https://ign.com/']

    def parse(self, response):
        """Follow links."""
        try:
            all_text = response.css('*:not(script):not(style)::text')
            for text in all_text:
                if self.query in text.get(): yield { 'url': response.request.url, 'text': text.get() }
        except: print(f'End of the line error for {self.name}.')

        yield from response.follow_all(css='a::attr(href)', callback=self.parse)

class BroadCrawler7(scrapy.Spider):
    """Broad crawling spider."""

    name = 'broad_crawler_7'
    start_urls = ['https://m.imdb.com']

    def parse(self, response):
        """Follow links."""
        try:
            all_text = response.css('*:not(script):not(style)::text')
            for text in all_text:
                if self.query in text.get(): yield { 'url': response.request.url, 'text': text.get() }
        except: print(f'End of the line error for {self.name}.')

        yield from response.follow_all(css='a::attr(href)', callback=self.parse)

class BroadCrawler8(scrapy.Spider):
    """Broad crawling spider."""

    name = 'broad_crawler_8'
    start_urls = ['https://m.imdb.com']

    def parse(self, response):
        """Follow links."""
        try:
            all_text = response.css('*:not(script):not(style)::text')
            for text in all_text:
                if self.query in text.get(): yield { 'url': response.request.url, 'text': text.get() }
        except: print(f'End of the line error for {self.name}.')

        yield from response.follow_all(css='a::attr(href)', callback=self.parse)

class BroadCrawler9(scrapy.Spider):
    """Broad crawling spider."""

    name = 'broad_crawler_9'
    start_urls = ['https://www.dictionary.com']

    def parse(self, response):
        """Follow links."""
        try:
            all_text = response.css('*:not(script):not(style)::text')
            for text in all_text:
                if self.query in text.get(): yield { 'url': response.request.url, 'text': text.get() }
        except: print(f'End of the line error for {self.name}.')

        yield from response.follow_all(css='a::attr(href)', callback=self.parse)