"""
Django settings for coffeedapp project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a6%(9x8@v=)266$k1h#e99at&^q@el8js@vljxp8_of%xu_a^4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages",
"django.core.context_processors.request"
)

# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'widget_tweaks',
	'core',
	'sitegate',
	'bootstrap3',
	'geoposition',
	'bootstrap_pagination',

)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'coffeedapp.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(MAIN_DIR, 'templates')],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'coffeedapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}
# Parse database configuration from $DATABASE_URL


print "CHECKING_HEROKU!"
ON_HEROKU = os.environ.get('ON_HEROKU') #<---- this captures the ON_HEROKU variable from the environment and assigns it to ON_HEROKU.


if ON_HEROKU == '1':
# Parse database configuration from $DATABASE_URL
    import dj_database_url
    print "ON_HEROKU!"
    DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
    }
else:
    print "NOT_ON_HEROKU!"
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(MAIN_DIR, 'db.sqlite3'),
        #'NAME': 'database.db',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        #'USER': '',
        #'PASSWORD': '',
        #'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        #'PORT': '',                      # Set to empty string for default.
    }
}

"""if ON_HEROKU == 1:

	# Parse database configuration from $DATABASE_URL

	import dj_database_url
	DATABASES['default'] = dj_database_url.config()

else: 

	DATABASES = {

		'default': {

			'ENGINE': 'django.db.backends.sqlite3',

			'NAME': os.path.join(MAIN_DIR, 'db.sqlite3'),

		}

	}

"""


#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

TEMPLATES_DIRS = (
	os.path.join(MAIN_DIR, 'templates'),
	)
STATICFILES_DIRS = (
os.path.join(MAIN_DIR, 'static'),

)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_FORCE_HTTP_URL = True
AWS_QUERYSTRING_AUTH = False
AWS_SECRET_ACCESS_KEY = os.environ.get('AWSSecretKey')
AWS_ACCESS_KEY_ID = os.environ.get('AWSAccessKeyId')

AWS_STORAGE_BUCKET_NAME = '1mopycoffeed'

