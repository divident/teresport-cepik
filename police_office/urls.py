from django.conf.urls import url

from . import views

app_name = 'police_office'
urlpatterns = [
    url(r'^$', views.CarListView.as_view(), name='index'),
    url(r'^(?P<pk>[A-Z0-9]+)/detail/$', views.CarDetailView.as_view(), name='detail'),
]
