import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

#Braintree Payments Details
BRAINTREE_PUBLIC = os.getenv('BRAINTREE_PUBLIC')
BRAINTREE_PRIVATE = os.getenv('BRAINTREE_PRIVATE')
BRAINTREE_MERCHANT_ID = os.getenv('BRAINTREE_MERCHANT_ID')
BRAINTREE_ENVIRONEMNT = os.getenv('BRAINTREE_ENVIRONEMNT')

#Email Config
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'