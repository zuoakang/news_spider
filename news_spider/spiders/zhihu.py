import json
import re

import scrapy

from news_spider.items import ZhihuItem
from news_spider.utils.common import get_category_by_name


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/billboard/']
    category_id = get_category_by_name(name)

    def parse(self, response):
        js_list = response.xpath("//script[@id='js-initialData']")
        if not js_list:
            yield
        js_data = js_list[0]
        js_string = js_data.extract()
        match = re.findall('<script id="js-initialData" type="text/json">(.*?)</script>', js_string, re.S)
        if not match:
            yield
        js_init = match[0]
        js_loads = json.loads(js_init)
        hot_list = js_loads['initialState']['topstory']['hotList']

        for hot_data in hot_list:
            item = ZhihuItem()
            target = hot_data["target"]
            title = target["titleArea"]["text"]
            hot_val = target["metricsArea"]["text"]
            img = target["imageArea"]["url"]
            url = target["link"]["url"]
            hot_val_cn = hot_val.replace(" ", "")
            hot_val_num = int(hot_val_cn.replace("万热度", "")) * 10000
            item["title"] = title
            item["hot_val"] = hot_val_cn
            item["url"] = url
            item["category_id"] = self.category_id
            item["rank"] = hot_val_num
            yield item
