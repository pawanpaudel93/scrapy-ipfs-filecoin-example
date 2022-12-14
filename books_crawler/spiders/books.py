from scrapy import Spider, Request
from books_crawler.items import Books

class BooksSpider(Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]

    start_urls = [
        "https://books.toscrape.com/catalogue/category/books/music_14/index.html"
    ]

    def parse(self, response):
        books = response.xpath("//h3/a/@href").extract()
        for book in books:
            absolute_url = response.urljoin(book)
            yield Request(absolute_url, callback=self.parse_book)

        # process next page
        # next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
        # absolute_next_page_url = response.urljoin(next_page_url)
        # yield Request(absolute_next_page_url)

    def parse_book(self, response):
        book = Books()
        title = response.xpath("//h1/text()").extract_first()
        price = response.xpath('//*[@class="price_color"]/text()').extract_first()

        image_url = response.xpath("//img/@src").extract_first()
        image_url = image_url.replace("../..", "http://books.toscrape.com")

        rating = response.xpath(
            '//*[contains(@class, "star-rating")]/@class'
        ).extract_first()
        rating = rating.replace("star-rating", "")

        # description = response.xpath('//*[@id="product_description"]/following-sibling::p/text()').extract_first()

        book["title"] = title
        book["price"] = price
        book["rating"] = rating.strip()
        book["image_urls"] = [image_url]

        yield book

