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

