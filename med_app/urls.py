from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.patient_list),
    url(r'^patient/(?P<pk>[0-9]+)/$', views.patient_detail),
]
