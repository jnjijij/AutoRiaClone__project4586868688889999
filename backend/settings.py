ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'your-domain.com']

MIDDLEWARE = [
    # ...
    'corsheaders.middleware.CorsMiddleware',
    # ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://your-domain.com",
]