from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<year>[0-9]+)/$', views.articles_by_year, name='year'),
    url(r'^(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', views.articles_by_month, name='month'),
    url(r'^(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$', views.articles_by_day, name='day'),
]
