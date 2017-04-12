from django.conf.urls import url
from .views import UserSignUpAPIView,UserLoginAPIView

urlpatterns = [
    url(r'^register/$', UserSignUpAPIView.as_view(),name='register'),
    url(r'^login/$', UserLoginAPIView.as_view(),name='login'),

]
