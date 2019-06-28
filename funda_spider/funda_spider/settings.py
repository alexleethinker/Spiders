# -*- coding: utf-8 -*-

# Scrapy settings for funda_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html


############ 如何自动获取cookies?


BOT_NAME = 'funda_spider'

SPIDER_MODULES = ['funda_spider.spiders']
NEWSPIDER_MODULE = 'funda_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
from funda_spider import user_agents
import random
USER_AGENT = random.choice(user_agents.agents)

from funda_spider import get_cookies 
cookies = {'_vis_opt_exp_67_combi': '2', '_vis_opt_exp_81_exclude': '1', '_ga': 'GA1.2.1502718080.1561463733', '_gid': 'GA1.2.1646304843.1561463733', '_vis_opt_s': '1%7C', 'SNLB2': '12-001', '_vwo_sn': '0%3A1', '_vis_opt_test_cookie': '1', '_vwo_ds': '3%3Aa_0%2Ct_0%3A0%241561463723%3A23.3810494%3A%3A%3A%3A1', 'D_ZID': 'B7582915-2342-3B54-9343-BC1DCE799E8E', 'satisfaction-survey-chance': '0.0403899275885848', 'fonts-loaded': 'true', 'INLB': '01-004', 'sr': '0%7cfalse', 'D_SID': '213.46.252.136:48rZgOaLq07BxrV0Qr6LtG+9ZX6f1oCFngMEVSQzTPk', 'D_UID': 'D644992F-2B1E-3E41-9DE9-F217B4362A49', '.ASPXANONYMOUS': '4V5eW9xpxKl3EkqZq8zIBv4lcHtHlKJzUXRaBTg5iCG5uOS5DfKvk0gLrD0PqmD1sknqjSbDyPTzkKIcVGWAfn4hfTnoLb8FBqUB1iW71ervGlotG8otKQ6aALP4MaNLDjjJUCLn1dz5YorxzHNosKif--g1', '_vwo_uuid_v2': 'D15EFEB276818AA2126C9C28B803EC581|b916da0e2f06e5601dfa81595da1a0aa', 'html-classes': 'js supports-placeholder', 'D_HID': 'A4A9E92C-2A48-3C2C-8A88-C4964FA76B91', 'D_IID': 'D383A0CE-44F4-3CD9-A86F-F857C5DAE6B6', 'D_ZUID': '03044E65-40B9-39DC-B123-50B3846BD9DA', '_vwo_uuid': 'D15EFEB276818AA2126C9C28B803EC581', '__RequestVerificationToken': 'tDON4sgpOIM-o_KwfC0sjX3NodUMYfxV7ZcnZLGxAMNlLJ8D9WrJLi0-aQAInnJeaDput6sP7jq1PanBIRBgzBJDo9c1'}
cookie_string = "; ".join([str(x)+"="+str(y) for x,y in cookies.items()])

#get_cookies.get_cookies()

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
#COOKIES_DEBUG =True
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:




DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,nl;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': cookie_string,
    'Host': 'www.funda.nl',
    'Referer': 'https://www.funda.nl/en/koop/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': USER_AGENT
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'funda_spider.middlewares.FundaSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 543,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware':543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'funda_spider.pipelines.FundaSpiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
'''
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
'''