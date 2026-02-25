# # import scrapy
# #
# #
# # # class BookSpider(scrapy.Spider):
# # #     name = 'bookspider'
# # #     start_urls = ['https://books.toscrape.com/catalogue/page-1.html']
# # #
# # #     def parse(self, response):
# # #         # Seleciona todos os livros da página
# # #         books = response.css('article.product_pod')
# # #         for book in books:
# # #             # Pega o link da página de detalhes
# # #             detail_page = book.css('h3 a::attr(href)').get()
# # #             yield response.follow(detail_page, self.parse_detail)
# # #
# # #     def parse_detail(self, response):
# # #         # Extraindo a descrição (o texto fica em um <p> logo após a div #product_description)
# # #         description = response.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
# # #
# # #         # Extraindo a URL da imagem (convertendo para URL absoluta)
# # #         image_relative_url = response.css('div.item.active img::attr(src)').get()
# # #         image_url = response.urljoin(image_relative_url)
# # #
# # #         yield {
# # #             'title': response.css('h1::text').get(),
# # #             'description': description,
# # #             'image_urls': [image_url],  # O Scrapy exige uma lista para o download automático
# # #         }
# #
# # class BooksSpider(scrapy.Spider):
# #     name = "response"
# #     primeira_pagina= 1
# #     def start_requests(self):
# #         yield scrapy.Request(url="https://books.toscrape.com/catalogue/page-1.html")
# #
# #     def parse(self, response):
# #
# #         response = response.xpath('//article[@class="product_pod"]')
# #
# #         for response in response:
# #             yield {
# #                 "titulo":  response.xpath('//article[@class="product_pod"]//h3/a/@title').getall(),
# #                 "preco":  response.xpath('//article[@class="product_pod"]//p[@class="price_color"]/text()').getall(),
# #                 "disponibilidade": response.xpath('//article[@class="product_pod"]//p[contains(@class,"instock")]/text()[normalize-space()]').getall(),
# #             }
# #
# #         next_page = response.xpath('//li[@class="next"]/a/@href').get()
# #
# #         if next_page:
# #             yield response.follow(next_page, callback=self.parse)
# import scrapy
#
#
# class BooksSpider(scrapy.Spider):
#     name = "books"
#     allowed_domains = ["books.toscrape.com"]
#     start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]
#
#     # def parse(self, response):
#     #     books = response.css('article.product_pod h3 a::attr(href)').getall()
#     #
#     #     for book in books:
#     #         link = response.urljoin(book)
#     #         yield scrapy.Request(link, callback=self.parse_book)
#     #
#     #     next_page = response.css('li.next a::attr(href)').get()
#     #     if next_page:
#     #         next_page_url = response.urljoin(next_page)
#     #         yield scrapy.Request(next_page_url, callback=self.parse)
#     #
#     # def parse_book(self, response):
#     #     yield {
#     #         'titulo': response.css('div.product_main h1::text').get(),
#     #         'preco': response.css('p.price_color::text').get(),
#     #         'descricao': response.css('#product_description ~ p::text').get(),
#     #         'categoria': response.css('ul.breadcrumb li:nth-child(3) a::text').get(),
#     #         'estoque': response.xpath('//article[@class="product_pod"]//p[contains(@class,"instock")]/text()[normalize-space()]').getall(),
#     #         'image_urls': (imagem_url)
#     #
#     #     }
#     #
#     def parse_book(self, response):
#
#         # 🔹 Pega imagem
#         imagem_relativa = response.css('div.item.active img::attr(src)').get()
#
#         if imagem_relativa:
#             imagem_url = response.urljoin(imagem_relativa)
#             image_urls = [imagem_url]
#         else:
#             image_urls = []
#
#         yield {
#             'titulo': response.css('div.product_main h1::text').get(),
#             'preco': response.css('p.price_color::text').get(),
#             'descricao': response.css('#product_description ~ p::text').get(),
#             'categoria': response.css('ul.breadcrumb li:nth-child(3) a::text').get(),
#             'estoque':response.css('p.instock.availability').xpath('normalize-space()').get(),
#             'image_urls': image_urls,
#         }
import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        # Pega todos os links dos livros
        for href in response.css("article.product_pod h3 a::attr(href)").getall():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_book)

        # Paginação
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_book(self, response):
        imagem_relativa = response.css('div.item.active img::attr(src)').get()
        if imagem_relativa:
            imagem_url = response.urljoin(imagem_relativa)
            image_urls = [imagem_url]
        else:
            image_urls = []

        yield {
            'titulo': response.css('div.product_main h1::text').get(),
            'preco': response.css('p.price_color::text').get(),
            'descricao': response.css('#product_description ~ p::text').get(),
            'categoria': response.css('ul.breadcrumb li:nth-child(3) a::text').get(),
            'estoque': response.css('p.instock.availability').xpath('normalize-space()').get(),
            'image_urls': image_urls,
        }
