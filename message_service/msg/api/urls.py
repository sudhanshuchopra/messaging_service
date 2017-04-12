from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^msg/$', views.MessageList.as_view()),
    url(r'^msg/(?P<pk>[0-9]+)/$', views.MessageDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)