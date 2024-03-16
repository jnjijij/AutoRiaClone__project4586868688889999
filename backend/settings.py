ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'your-domain.com']

MIDDLEWARE = [
    # ...
    'corsheaders.middleware.CorsMiddleware',
    # ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://your-domain.com",
]
INSTALLED_APPS = [
    # ...
    'channels',
    'cms',
    'menus',
    "consumer",
    'ad_info'
    # ...
]
ASGI_APPLICATION = 'autoria_clone.routing.application'

CMS_TEMPLATES = [
    {
        'BACKEND': 'cms.templates.django.DjangoTemplateBackend',
        'APP_DIRS': True,
        'DIRS': [],
    },
]
