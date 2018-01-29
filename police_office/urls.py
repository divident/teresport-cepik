from django.conf.urls import url

from . import views

app_name = 'police_office'
urlpatterns = [
    url(r'^$', views.PoliceCarListView.as_view(), name='index'),
    url(r'^(?P<pk>[A-Z0-9]+)/detail/$', views.PoliceCarDetailView.as_view(), name='detail'),
]
