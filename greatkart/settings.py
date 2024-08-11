import os
from pathlib import Path
from dotenv import load_dotenv
from django.contrib.messages import constants as messages


# Load environment variables from a .env file
load_dotenv()

# Base directory of the Django project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key (Keep this secret!)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-default-secret-key')

# Debug mode for development (Set to False in production)
DEBUG = os.getenv('DJANGO_DEBUG', 'False').lower() == 'true'

# Allowed hosts for production
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# List of installed apps in your project
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'category',
    'accounts',
    'store',
    'carts',
    'orders',
   #'jet',
   # #'grappelli',
    #'suit',
   # 'admin_plus',
    # Add more apps as needed
]

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration for your project
ROOT_URLCONF = 'greatkart.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.menu_links',
                'carts.context_processors.counter',
            ],
        },
    },
]

# WSGI application for serving your project
WSGI_APPLICATION = 'greatkart.wsgi.application'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model for authentication
AUTH_USER_MODEL = 'accounts.Account'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),  # Ensure this is a string
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization and localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, etc.) settings
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # For collecting static files
STATICFILES_DIRS = [BASE_DIR / 'static']  # Additional directories for static files

# Media files (user-uploaded content) settings
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Message tags configuration for styling (using Bootstrap classes)
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# Email settings for SMTP (using Gmail as an example)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'your-email@gmail.com')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'your-email-password')

# Logging configuration for database operations (enabled in DEBUG mode)
if DEBUG:
    import logging
    logger = logging.getLogger('django.db.backends')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
