

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jnjijij',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'your-rds-endpoint',
        'PORT': '5432',
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://your-elasticache-endpoint:6379/0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
STATIC_URL = 'https://your-cloudfront-domain.cloudfront.net/static/'
MEDIA_URL = 'https://your-cloudfront-domain.cloudfront.net/media/'