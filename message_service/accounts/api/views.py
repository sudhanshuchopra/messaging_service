from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from .serializers import UserSignUpSerializer,UserLoginSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny

User=get_user_model()

class UserSignUpAPIView(CreateAPIView):
	serializer_class=UserSignUpSerializer
	queryset=User.objects.all()


class UserLoginAPIView(APIView):
	permission_classes=[AllowAny]
	serializer_class=UserLoginSerializer

	def post(self,request,*args,**kwargs):
		data=request.data
		serializer=UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			validated_data=serializer.data
			return Response(validated_data,status=HTTP_200_OK)
		return response(serializer.errors, status=HTTP_400_BAD_REQUEST)
