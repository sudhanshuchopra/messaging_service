from django.conf.urls import url
from .views import UserSignUpAPIView

urlpatterns = [
    url(r'^register/$', UserSignUpAPIView.as_view(),name='register'),

]
