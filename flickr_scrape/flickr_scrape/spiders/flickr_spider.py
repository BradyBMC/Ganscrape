import scrapy

# from flickr.items import FlickrItem

class FlickrSpider(scrapy.Spider):
    name = "flickr"
    #allowed_domains = ['flickr.com']
    start_urls = ['https://www.flickr.com/search/?text=gamecube%20controller%20orange']

    def parse(self, response):
        raw_data = response.css('.photo-list-photo-view.awake').getall()
        url = []
        for image_data in raw_data:
            begin = image_data.find('//')
            end = image_data.find(')', begin)
            url.append('https:'+ image_data[begin:end])

        yield {
            'image_urls' : url,
            'image_name' : 'flickr'
        }
