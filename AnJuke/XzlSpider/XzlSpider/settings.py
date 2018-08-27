# -*- coding: utf-8 -*-

# Scrapy settings for XzlSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'XzlSpider'

SPIDER_MODULES = ['XzlSpider.spiders']
NEWSPIDER_MODULE = 'XzlSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Article (+http://www.yourdomain.com)'
#使用scrapy-redis里的去重组件，不使用scrapy默认的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#使用scrapy-redis里的调度器组件，不使用scrapy默认的去重
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True

# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'XzlSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 4

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

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
#    'XzlSpider.middlewares.XzlspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'XzlSpider.middlewares.XzlspiderDownloaderMiddleware': 543,
   #  'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'XzlSpider.middlewares.UserAgentMiddleware':444,
    'XzlSpider.middlewares.ProxyMiddleware':543,
    # 'XzlSpider.middlewares.ThreatDefenceRedirectMiddleware':600,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'XzlSpider.pipelines.XzlspiderPipeline': 300,
   #  'scrapy_redis.pipelines.RedisPipeline': 300,
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


# SCHEDULER = "scrapy_redis.scheduler.Scheduler"  #启用Redis调度存储请求队列
# SCHEDULER_PERSIST = True    #不清除Redis队列、这样可以暂停/恢复 爬取
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  #确保所有的爬虫通过Redis去重
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
REDIS_HOST = 'localhost'  # 也可以根据情况改成 localhost
REDIS_PORT = 6379
REDIS_PARAMS = {
   # 'password': 在此设置密码,
   'db': 11
}
REDIS_URL = None
#防止反爬
CONCURRENT_REQUESTS = 5
# DOWNLOAD_DELAY = 1.2
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
# REDIRECT_ENABLED = False






MONGO_URI = '192.168.0.21'
MONGO_DATABASE = 'AnJuKeXzl'












NEWHOUSE ={
    '日租金':'daily_hire',
    '月租金':'month_hire',
    '得房率':'get_house',
    '楼盘名':'house_name',
    '地址':'address',
    '地铁':'subway',
    '建筑面积':'covered_area',
    '楼层':'floor',
    '工位数':'station',
    '物业费':'property_management_fee',
    '类型':'type',
    '总楼层':'total_floor',
    '竣工年月':'completion_date',
    '大堂层高':'lobby_height',
    '空调类型':'air_conditioning_type',
    '车位':'parking_space',
    '单层面积':'every_area',
    # '得房率':'get_house',
    '物业公司':'property_company',
    '标准层高':'standard_floor_hegiht',
    '电梯':'elevator',
    '是否涉外':'is_foregin',
    '单价':'unit_price',
    '总价':'total_price',
    '面积':'area',
    '省份':'province',
    '市':'city',
    '县':'county',
    '预估月支出':'estimated_monthly_expenditure',
}