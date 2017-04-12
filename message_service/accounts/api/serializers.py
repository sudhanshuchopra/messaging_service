from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.db.models import Q
from rest_framework import serializers

User=get_user_model()


class UserSignUpSerializer(ModelSerializer):
	class Meta:
		model=User
		fields=['username','password']
		extra_kwargs={
		"password":{
		"write_only":True
		}
		}
	def create(self,validated_data):
		username=validated_data['username']
		password=validated_data['password']
		user_obj=User(username=username)
		user_obj.set_password(password)
		user_obj.save()
		return validated_data

class UserLoginSerializer(ModelSerializer):
	token=serializers.CharField(allow_blank=True,read_only=True)
	username=serializers.CharField()
	class Meta:
		model=User
		fields=['username','password','token']
		extra_kwargs={
		"password":{
		"write_only":True
		}
		}
	def validate(self,data):
		username=data.get("username")
		password=data['password']
		user=User.objects.filter(Q(username=username))
		if user.exists() and user.count()==1:
			user=user.first()
		else:
			raise serializers.ValidationError("this username is not valid")
		if user:
			if not user.check_password(password):
				raise serializers.ValidationError("incorrect creditionals")
		data['token']="some random token"
		return data


class UserDetailSerializer(ModelSerializer):
	class Meta:
		model=User
		fields=['username',]

