
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


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


class Attempts(models.Model):
	attemptId = models.AutoField(primary_key=True)
	q_name=models.CharField(max_length=500, default="",null=True)
	qAttempter=models.CharField(max_length=500, default="",null=True)
	totalQue=models.IntegerField(default= 0 )
	attemptedQue=models.IntegerField(default= 0)
	correct=models.IntegerField(default= 0)
	accuracy=models.IntegerField(default= 0)
	attemptedtime=models.DateTimeField(default=datetime.now())
	
	def __str__(self):
		return str(self.attemptId)


class Test(quiz):
	testId = models.CharField(max_length=500)
	def __str__(self):
		return str(self.testId)