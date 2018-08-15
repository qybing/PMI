# -*- coding: utf-8 -*-

# Scrapy settings for XpSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'XpSpider'

SPIDER_MODULES = ['XpSpider.spiders']
NEWSPIDER_MODULE = 'XpSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'XpSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 4

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
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
#    'XpSpider.middlewares.XpspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'XpSpider.middlewares.XpspiderDownloaderMiddleware': 543,
    'XpSpider.middlewares.RandomProxy':543,
    'XpSpider.middlewares.UserAgentMiddleware':444,
    # 'XpSpider.middlewares.ProxyMiddleware':543
}



#使用scrapy-redis里的去重组件，不使用scrapy默认的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#使用scrapy-redis里的调度器组件，不使用scrapy默认的去重
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True







# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'XpSpider.pipelines.XpspiderPipeline': 300,
    # 'scrapy_redis.pipelines.RedisPipeline': 400,
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
   'db': 8
}
#防止反爬
DOWNLOAD_DELAY = 2

RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
#重试次数
RETRY_TIMES= 3
#下载时间设置
DOWNLOAD_TIMEOUT = 15
#使用集合对start_requests去重
REDIS_START_URLS_AS_SET = True









MONGO_URI = 'localhost'
MONGO_DATABASE = 'AnJuKe'


# MONGODB_HOST = '127.0.0.1'
# MONGODB_PORT = 27017
# MONGODB_DBNAME = 'AnJuKe'
# MONGODB_DOCNAME = 'xp'

NEWHOUSE = {'楼盘名称': 'property_name',
                 '楼盘特点': 'property_features',
                 '参考单价': 'reference_unit_price',
                 '物业类型': 'property_type',
                 '开发商': 'developer',
                 '区域位置': 'regional_location',
                 '楼盘地址': 'property_address',
                 '售楼处电话': 'sales_office_phone',
                 '最低首付': 'minimum_down_payment',
                 '开间面积': 'opening_area',
                 '办公室面积': 'office_area',
                 '楼盘户型': 'real_estate_type',
                 '招租客群': 'tenant_group',
                 '临近CBD': 'near_cbd',
                 '已签约租户': 'contracted_tenant',
                 '公共部分精装修': 'public_decoration',
                 '标准层面积': 'standard_floor_area',
                 '写字楼类型': 'office_type',
                 '写字楼级别': 'office_level',
                 '规划户数': 'number_of_planned_households',
                 '楼盘总价': 'total_price_of_the_property',
                 '绿化率': 'greening_rate',
                 '商业面积': 'commercial_area',
                 '总建筑面积': 'total_surface_area',
                 '最新开盘': 'latest_opening',
                 '交房时间': 'delivery_time',
                 '招商业态': 'business_mode',
                 '已签约商户': 'contracted_merchant',
                 '临近商圈': 'near_business_district',
                 '周边人群': 'surrounding_crowd',
                 '售楼处地址': 'sales_office_address',
                 '预售许可证': 'presale_permit',
                 '产权年限': 'year_of_property_rights',
                 '出售类型': 'type_of_sale',
                 '得房率': 'toom_rate',
                 '总套数': 'total_number_of_sets',
                 '楼层状况': 'floor_condition',
                 '工程进度': 'project_progress',
                 '物业管理费': 'property_management_fees',
                 '物业公司': 'property_company',
                 '车位数': 'number_of_car',
                 '车位比': 'parking_ratio',
                 '是否统一管理': 'uniform_management',
                 '是否分割': 'whether_to_split',
                 '出租类型': 'type_of_rental',
                 '租金': 'rent',
                 '是否包含物业费': 'include_property_fees',
                 '待租面积': 'area_to_be_rented',
                 '待租套数': 'number_of_rents_to_be_rented',
                 '省份': 'province',
                 '城市': 'city',
                 '区': 'county',
                '建筑类型':'building_type',
                '月供':'monthly_supply'
                 }

