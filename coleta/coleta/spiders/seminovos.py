import scrapy


class SeminovosSpider(scrapy.Spider):
    name = "seminovos"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/veiculos/carros-caminhonetes-em-sao-paulo/_PriceRange_0-40000_NoIndex_True_VEHICLE*TYPE_398351#applied_filter_id%3Dstate%26applied_filter_name%3DLocaliza%C3%A7%C3%A3o%26applied_filter_order%3D6%26applied_value_id%3DTUxCUFNBT085N2E4%26applied_value_name%3DS%C3%A3o+Paulo%26applied_value_order%3D15%26applied_value_results%3D18163%26is_custom%3Dfalse~"]

    def parse(self, response):
        pass
