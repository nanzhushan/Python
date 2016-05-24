#coding:utf8

from django.conf.urls import include, url
from django.contrib import admin
from xxoo import views

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^get/$',views.get)
]
