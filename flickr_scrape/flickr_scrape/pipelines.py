# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class customImagePipeline(ImagesPipeline):
    # COnfused how get_media_request works/is called
    def get_media_requests(self, item, info):
        i = 0
        for image_url in item['image_urls']:
            filename = '{}_{}.jpg'.format(item['image_name'], i)
            yield scrapy.Request(image_url, meta={'filename': filename})
            i += 1
        return

    def file_path(self, request, response=None, info=None):
        return request.meta['filename']

    # def file_path(self, request, response=None, info=None, *, item=None):
    #     dic = item.get('count')
    #     if(len(dic) > 0):
    #         count = dic[0]
    #         dic.pop(0)
    #     else:
    #         count = 69
    #     image_filename = f'{count}_image.jpg'
    #     return image_filename
