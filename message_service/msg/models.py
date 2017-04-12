from django.db import models

# Create your models here.
from django.conf import settings

class Message(models.Model):
	creator=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='created_by')
	recipent=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='recieved_by')
	content=models.TextField()
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
	updated=models.DateTimeField(auto_now=True,auto_now_add=False)