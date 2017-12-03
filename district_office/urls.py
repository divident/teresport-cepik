from django.conf.urls import url

from . import views

app_name = 'district_office'
urlpatterns = [
  url(r'^$', views.CarListView.as_view(), name='index'),
  url(r'^(?P<pk>[A-Z0-9]+)/detail/$', views.CarDetailView.as_view(), name='detail'),
  url(r'^health/$', views.HealthExaminationListView.as_view(), name='health'),
  url(r'^health/(?P<pk>[A-Z0-9]+)/detail/$', views.OutdatedHealthExaminationView.as_view(), name='outdated'),
]
