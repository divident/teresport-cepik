from django.conf.urls import url

from . import views

app_name = 'district_office'
urlpatterns = [
  url(r'^$', views.CarListView.as_view(), name='index'),
  url(r'^(?P<pk>[A-Z0-9]+)/detail/$', views.CarDetailView.as_view(), name='detail'),
  url(r'^add/$', views.CarAdd.as_view(), name='add'),
  url(r'^card/(?P<car_id>[A-Z0-9]+)/$', views.card_generation_view, name='card'),
]
