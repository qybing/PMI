# -*- coding: utf-8 -*-

# Scrapy settings for SpZu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'SpZu'

SPIDER_MODULES = ['SpZu.spiders']
NEWSPIDER_MODULE = 'SpZu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'SpZu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy
#并发数
# CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'SpZu.middlewares.SpzuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'SpZu.middlewares.SpzuDownloaderMiddleware': 543,
    'SpZu.middlewares.UserAgentMiddleware':421,
    'SpZu.middlewares.ProxyMiddleware':415,
    # 'SpZu.middlewares.RandomProxy':415

}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}





#使用scrapy-redis里的去重组件，不使用scrapy默认的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#使用scrapy-redis里的调度器组件，不使用scrapy默认的去重
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True





# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"
# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'SpZu.pipelines.SpzuPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline':400,
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
REDIS_HOST = '127.0.0.1'  # 主机ip
REDIS_PORT = 6379
REDIS_PARAMS = {
   # 'password': 在此设置密码,
   'db': 2
}


#设置重定向参数
# REDIRECT_ENABLED = False


# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"
#防止反爬
DOWNLOAD_DELAY = 2

RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
#重试次数
RETRY_TIMES= 3
#下载时间设置
DOWNLOAD_TIMEOUT = 15
#使用集合对start_requests去重
REDIS_START_URLS_AS_SET = True

























SP_HOSER = {
        '总价': 'total_price',
        '单价': 'unit_price',
        '预期租金收益': 'expected_rental_income',
        '月租': 'monthly_rent',
        '转让费': 'transfer_fee',
        '物业费': 'property_management_fee',
        '面积': 'area',
        '面宽': 'face_width',
        '层高': 'layer_height',
        '进深': 'depth',
        '楼层': 'floor',
        '状态': 'status',
        '起租期': 'lease_period',
        '人群': 'crowd',
        '押付': 'pay',
        '免租期': 'rent_free_period',
        '地址': 'address',
        '是否临街': 'is_face_street',
        '商铺名字': 'shop_name',
        '开发商': 'developer',
        '物业公司': 'property_company',
        '统一管理': 'unified_management',
        '竣工时间': 'completion_time',
        '总楼层': 'total_floor',
        '总面积': 'total_area',
    }