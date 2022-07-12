# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
import scrapy

from PIL import Image

# Copy over image file location
from flickr_scrape.settings import IMAGES_STORE

class customImagePipeline(ImagesPipeline):
    # Confused how get_media_request works/is called
    def get_media_requests(self, item, info):
        i = 0
        for image_url in item['image_urls']:
            filename = '{}_{}.jpg'.format(item['image_name'], i)
            yield scrapy.Request(image_url, meta={'filename': filename})
            i += 1
        return

    def file_path(self, request, response=None, info=None):
        return request.meta['filename']

    def convert(height, width, size):
        nh = (height - size)/2
        nw = (height - size)/2
        return (nh, nw, nh + size, nw + size)

    def item_completed(self, results, item, info):
        for result, image_info in results:
            if result:
                path = IMAGES_STORE + '/' + image_info['path']
                img = Image.open(path)
                height, width = img.size
                if(height > 1024 and width > 1024):
                    img = img.crop(self.convert(height, width, 1024))
                elif(height > 512 and width > 512):
                    img = img.crop(self.convert(height, width, 512))
                else:
                    img = img.resize((256, 256))
                img.save(path)
        return item
