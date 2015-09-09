# -*- coding: utf-8 -*- 

"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ik3aclhd!j+oe!#n(d^94d-hr5qp68(0on(#$ezzrqayg)86^h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stucheck',
    'statistic',
    'phone',
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.core.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stuget',
        'USER': 'root',
        'PASSWORD': '3783Aa',
        'HOST': 'localhost',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh_CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


SUIT_CONFIG = {
    # header
    'ADMIN_NAME': u'汕大GET',
    'HEADER_DATE_FORMAT': 'l, M j, Y',
    'HEADER_TIME_FORMAT': 'g:i A',
    # menu
    'MENU': (
        'sites',
        {'app': 'auth', 'label': u'认证管理', 'icon': 'icon-user', 'models': (
            {'model': 'auth.user', 'label': u'用户'},
            {'model': 'auth.group', 'label': u'组'},
        )},
        {'app': 'phone', 'label': u'电话查询', 'models':(
            {'model': 'phone.category', 'label': u'分类'},
            {'model': 'phone.phonelist', 'label': u'电话'},
            {'model': 'phone.version', 'label': u'版本'},
        )},
        {'app': 'phone', 'label': u'STUCHECK', 'models':(
            {'model': 'stucheck.userlist', 'label': u'认证用户'},
        )},
        {'app': 'statistic', 'icon': 'icon-question-sign', 'label': u'数据统计', 'models':(
            {'model': 'statistic.phone', 'label': u'电话查询'},
        )},
    ),
    # config
    'CONFIRM_UNSAVED_CHANGES': True,
}
