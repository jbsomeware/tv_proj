from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.show_list),
    url(r'^shows/new$', views.add_new_show),
    url(r'^shows/create$', views.create),
    url(r'^shows/(?P<val>\d+)$', views.show_info),
    url(r'^shows/(?P<val>\d+)/edit$', views.show_edit),
    url(r'^shows/(?P<val>\d+)/update$', views.show_update),
    url(r'^shows/(?P<val>\d+)/destroy$', views.show_delete),
]