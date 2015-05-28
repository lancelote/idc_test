from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.patient_list),
    url(r'^patient/(?P<pk>[0-9]+)/$', views.patient_detail),
    url(r'^patient/new/$', views.patient_new, name='patient_new'),
    url(r'^patient/(?P<pk>[0-9]+)/edit/$', views.patient_edit,
        name='patient_edit'),
]
