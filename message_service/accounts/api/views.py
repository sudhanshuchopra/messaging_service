from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from .serializers import UserSignUpSerializer


User=get_user_model()

class UserSignUpAPIView(CreateAPIView):
	serializer_class=UserSignUpSerializer
	queryset=User.objects.all()
	