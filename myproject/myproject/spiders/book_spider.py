import scrapy
import csv

class MySpider(scrapy.Spider):
    name = 'book_spider.py'
    start_urls = ['http://books.toscrape.com']

    def __init__(self):
        self.file = open('books_data.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['category', 'title', 'price', 'stock', 'image']) 

    def parse(self, response):
        categories = response.css('div.side_categories ul li ul li a::attr(href)').getall()
        for category in categories:
            category_url = response.urljoin(category)
            yield scrapy.Request(category_url, callback=self.parse_category)

    def parse_category(self, response):
        category_name = response.css('div.page-header.action h1::text').get()
        
        if category_name:
            category_name = category_name.strip()
        else:
            category_name = 'Unknown Category'

        books = response.css('article.product_pod')
        for book in books:
            image = book.css('div.image_container a img::attr(src)').get() 
            title = book.css('h3 a::attr(title)').get() 
            price = book.css('p.price_color::text').get() 
            stock = ''.join(book.css('p.instock.availability *::text').getall())

            title = title.strip() if title else 'N/A' 
            price = float(price.replace('£', '').strip()) if price else 'N/A' 
            image = image.strip() if image else 'N/A' 
            stock = stock.strip().replace('\n', '').replace('\r', '') if stock else 'N/A'

            self.writer.writerow([category_name, title, price, stock, image])

            yield {
                'category': category_name,
                'title': title,
                'price': price,
                'stock': stock,
                'image': image
            }

        next_page = response.css('li.next a::attr(href)').get() 
        if next_page: 
            yield response.follow(next_page, self.parse_category)

    def close(self, spider):
        self.file.close()
