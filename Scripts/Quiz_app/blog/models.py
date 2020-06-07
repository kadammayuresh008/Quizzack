
from django.db import models
from django.contrib.auth.models import User


class quiz(models.Model):
	question=models.CharField(max_length=500, default="")
	option1=models.CharField(max_length=100, default="")
	option2=models.CharField(max_length=100, default="")
	option3=models.CharField(max_length=100, default="")
	option4=models.CharField(max_length=100, default="")
	answer=models.CharField(max_length=100, default="")
	catogaries=models.CharField(max_length=100,default="")
	student=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.catogaries