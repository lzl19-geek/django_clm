from .base import *
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
         'NAME': 'djangoelm',
         'USER': 'root',
         'PASSWORD': 'injury678',
         'PORT': 3306,
    }
}

# 以下为新增
# django的缓存配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # 提升Redis解析性能
            "PARSER_CLASS": "redis.connection.HiredisParser",
        }
    }
}

# 百度地图AK，申请服务端
# 申请网址：http://lbsyun.baidu.com/apiconsole/key/create
# BAIDU_AK = 'p0C5pNxcBpu7hYebHbkRqALvTltOX3OD'
BAIDU_AK = 'w9XHmXlX0kkRcxw8HE2mAbN24Fpn5H57'

# 发送邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# SMTP服务地址，使用其他服务器需更换
# EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
# 发送邮件的邮箱，换成自己的
# EMAIL_HOST_USER = 'clmwm@163.com'
EMAIL_HOST_USER = '2818111237@qq.com'
# 在邮箱中设置的客户端授权密码，换成自己的
EMAIL_HOST_PASSWORD = 'qqotczsvbbzddcei'
# 收件人看到的发件人，<>中地址必须与上方保持一致
EMAIL_FROM = 'c0c<2818111237@qq.com>'
