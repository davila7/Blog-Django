"""
Django settings for dblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iayz__i9ce_!qv5q6&z27cq_1^m3#5ch!rinf%@)a50_*d5f&3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'django_markdown',
    'gunicorn',
    'dj_database_url',
    'psycopg2',
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dblog.urls'

WSGI_APPLICATION = 'dblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# variables de autentificacion 
AUTHENTICATION_BACKENDS = (
        'social.backends.facebook.FacebookAppOAuth2',
        'social.backends.facebook.FacebookOAuth2',
        'social.backends.twitter.TwitterOAuth',
        'social.backends.github.GithubOAuth2',
        'social.backends.google.GoogleOAuth2',
        'django.contrib.auth.backends.ModelBackend',
    )

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

#TWITTER
SOCIAL_AUTH_TWITTER_KEY = 'DAEAQLJla7WvSsJjvMlmXZEhT'
SOCIAL_AUTH_TWITTER_SECRET = 'b2IPr4YO9fbYX5Eus1bSl2KhXYB5uqZx3pzoll6C7PrKe6XCHT'

#FACEBOOK
SOCIAL_AUTH_FACEBOOK_KEY = '1543179569281687'
SOCIAL_AUTH_FACEBOOK_SECRET = '177b5b692b7b4f64c185c869915e495d'

#GITHUB
SOCIAL_AUTH_GITHUB_KEY = '80da78cbd76b151d5c28'
SOCIAL_AUTH_GITHUB_SECRET = '90ae70435330e5ac97bff633540083c64c7ea1cb'
SOCIAL_AUTH_GITHUB_SCOPE = ['user:email']

#GOOGLE
GOOGLE_OAUTH2_CLIENT_ID = '959593380702-e6t938qmdnem6mi9uc6d2dnit00ll5g6.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'Cla4QCwLauybLKl2nm77udKz'


