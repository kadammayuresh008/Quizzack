from django.shortcuts import render,HttpResponse
from .models import quiz
from user.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
	return render(request,'blog/home.html')

def about(request):
	return render(request,'blog/about.html')

def catogaries(request):
	y= quiz.objects.all().values('catogaries')
	x=list(y)
	a=[]
	for i in x:
		a.append(i['catogaries'])
	z=set(a)
	context={
	'quizs' :z,
	}
	return render(request,'blog/quiz_catlog.html',context)

def quiz_page(request):
	if request.method=='POST':
		data=request.POST
		datas= dict(data)
		try:
			x=quiz.objects.filter(catogaries=datas['que'][0])
		except:
			messages.success(request,f'Category not selected.')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	context1={
	'score':x[0],
	 'quizs':x,
	}
	return render(request,'blog/quiz_page.html',context1)

def quiz_page_result(request):
	print("result page")
	if request.method=='POST':
		data=request.POST
		datas= dict(data)
		qid=[]
		qans=[]
		ans=[]
		score=0
		for key in data:
			try:
				qid.append(int(key))
				qans.append(datas[key][0])
			except:
				print("Crsf")
		for q in qid:
			ans.append((quiz.objects.get(id = q)).answer)
		total=len(ans)
		for i in range(total):
			if ans[i] == qans[i]:
				score += 1
		print(score)
		eff=(score/total)*100
	context={
	'score':score,
	'total':total,
	'eff':eff,
	'sub':total-score,
	}
	return render(request,'blog/result.html',context)


def questionUpload(request):
	return render(request,'blog/Questionupload.html')

def Uploaded(request):
	if(request.method=="POST"):
		Question=request.POST.get("Question")
		Option1=request.POST.get("option")
		Option2=request.POST.get("option1")
		Option3=request.POST.get("option2")
		Option4=request.POST.get("option3")
		Answer=request.POST.get("Answer")
		Catogaries=request.POST.get("Category")
		Student=request.user

		question=quiz(question=Question,option1=Option1,option2=Option2,option3=Option3,option4=Option4,answer=Answer,catogaries=Catogaries,student=Student)
		question.save()
	messages.success(request,f'Question added successfully.')
	return render(request,'blog/Questionupload.html')