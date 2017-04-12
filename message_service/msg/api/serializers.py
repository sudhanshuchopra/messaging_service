from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from msg.models import Message

class MessageSerializer(ModelSerializer):
	creator = serializers.ReadOnlyField(source='creator.username')
	class Meta:
		model=Message
		fields=['creator','recipent','content']

