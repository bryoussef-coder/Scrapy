import scrapy


class DronesspiderSpider(scrapy.Spider):
    name = 'dronesspider'
    allowed_domains = ['jessops.com/drones']
    start_urls = ['http://jessops.com/drones/']

    def parse(self, response):
        products = response.css('div.details-pricing')  ## c'est pour extraire tous les données dans une variable
        for product in products:
            item = {
                'name': product.css('a::text').get(),
                'price': product.css('p.price.larger::text').get().replace(',', '')
            }
            yield item
        pass


class MaterielspiderSpider(scrapy.Spider):
    name = 'materielspider'
    allowed_domains = ['materiel.net/recherche/GeForce%20GTX']
    start_urls = ['https://www.materiel.net/recherche/GeForce%20GTX/']

    def parse(self, response):
        mproducts = response.css('ul.list-unstyled.c-products-list.c-products-list__row.mb-3')
        for mproduct in mproducts:
            mitem = {
                'carte': mproduct.css('h2::text').get(),
                'prix': mproduct.css('span.o-product__price::text').get()
            }
            yield mitem
        pass
