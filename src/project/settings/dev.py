import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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