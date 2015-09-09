from django.conf.urls import *
from phone.views import phoneData

urlpatterns = [
    url(r'^phonelist.json$', phoneData),
]