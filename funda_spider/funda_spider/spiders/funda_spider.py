#!/usr/bin/env python
# -*- encoding: utf-8 -*-


# 从index页面获取所有detail页面的链接   https://gist.github.com/1060460048/40b8734bb26e37c7b7e7cabfde29ae21
# 爬取detail页面的所有数据
# 储存进Mongo数据库

# 自动ip代理
# 自动获取cookies，自动判别失效，并从新获取
# 可能会有验证码
# scrapy-redis分布式
# scrapy-splash动态页面

# 状态变动




from funda_spider.items import FundaSpiderItem
import scrapy
from scrapy.selector import Selector


class FundaSpider(scrapy.Spider):
    name = "funda_spider"
    allowed_domains = ["www.funda.nl"]
    start_urls = [
        "https://www.funda.nl/en/koop/heel-nederland/"
        #"https://www.funda.nl/en/koop/maastricht/huis-86655999-gersthegge-34/"
    ]


    def parse(self, response) :
        '''
        filename = './results/index_1.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        '''

        #html = response.body

        sel = Selector(response)

        print(sel)

        #films = sel.xpath('//table[contains(@class, "results")]//tr[contains(@class, "detailed")]')
        #yield scrapy.Request(response.url,callback=self.parse)