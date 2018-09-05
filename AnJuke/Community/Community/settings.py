# -*- coding: utf-8 -*-

# Scrapy settings for Community project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Community'

SPIDER_MODULES = ['Community.spiders']
NEWSPIDER_MODULE = 'Community.spiders'



#使用scrapy-redis里的去重组件，不使用scrapy默认的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#使用scrapy-redis里的调度器组件，不使用scrapy默认的去重
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Community (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

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
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
#   # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   # 'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Community.middlewares.CommunitySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'Community.middlewares.CommunityDownloaderMiddleware': 543,
    'Community.middlewares.UserAgentMiddleware':501,
    'Community.middlewares.ProxyMiddleware':511
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Community.pipelines.CommunityPipeline': 300,
}

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
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
HTTPERROR_ALLOW_ALL =True


REDIS_HOST = 'localhost'  # 也可以根据情况改成 localhost
REDIS_PORT = 6379
REDIS_PARAMS = {
   # 'password': 在此设置密码,
   'db': 4
}
REDIS_URL = None
#防止反爬
CONCURRENT_REQUESTS = 5
DOWNLOAD_DELAY = 5.2
#状态码
HTTPERROR_ALLOW_ALL =True
# HTTPERROR_ALLOWED_CODES = [302,500, 503, 504, 400, 403, 404, 408]
# RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
#重试次数

RETRY_TIMES= 3
#下载时间设置
DOWNLOAD_TIMEOUT = 15
#使用集合对start_requests去重
REDIS_START_URLS_AS_SET = True



MONGO_URI = '192.168.0.21'
MONGO_DATABASE = 'AnJuKeArea'






HOUSE = {
            '物业类型': 'property_type',
            '物业费': 'property_costs',
            '总建面积': 'total_area',
            '总户数': 'total_houses',
            '建造年代': 'construction_age',
            '停车位': 'park',
            '容积率': 'volume_rate',
            '绿化率': 'greening_rate',
            '开发商': 'developer',
            '物业公司': 'property_company',
            '相关学校':'school',
        }