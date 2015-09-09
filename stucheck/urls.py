from django.conf.urls import *
from stucheck.views import loginCheck

urlpatterns = [
    url(r'^logincheck.json$', loginCheck),
]