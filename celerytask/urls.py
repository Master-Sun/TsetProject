from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'do/$', do, name="do"),
]