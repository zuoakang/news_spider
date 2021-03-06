# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class NewsSpiderBaseItem(scrapy.Item):
    title = Field()
    url = Field()
    hot_val = Field()
    rank = Field()
    category_id = Field()


class BaiduTopItem(NewsSpiderBaseItem):
    pass


class WeiboItem(NewsSpiderBaseItem):
    pass


class ZhihuItem(NewsSpiderBaseItem):
    pass

class PengPaiItem(NewsSpiderBaseItem):
    pass

class TxItem(NewsSpiderBaseItem):
    pass


class WangYiItem(NewsSpiderBaseItem):
    pass


class ToutiaoItem(NewsSpiderBaseItem):
    pass

class Kr36Item(NewsSpiderBaseItem):
    pass

class SspaiItem(NewsSpiderBaseItem):
    pass

class IthomeItem(NewsSpiderBaseItem):
    pass

class HuxiuItem(NewsSpiderBaseItem):
    pass


class CnbetaItem(NewsSpiderBaseItem):
    pass


class XueqiuItem(NewsSpiderBaseItem):
    pass

class WallstreetcnItem(NewsSpiderBaseItem):
    pass

class SmzdmItem(NewsSpiderBaseItem):
    pass

class JuejinItem(NewsSpiderBaseItem):
    pass

class V2exItem(NewsSpiderBaseItem):
    pass

class GelonghuiItem(NewsSpiderBaseItem):
    pass

class YicaiItem(NewsSpiderBaseItem):
    pass