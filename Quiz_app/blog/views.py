from django.shortcuts import render,HttpResponse
from .models import quiz,Attempts,Test
from user.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Quiz_app.settings import MEDIA_URL 

quizList=[]
testId=0

def home(request):
	return render(request,'blog/home.html')

@login_required
def about(request):
	return render(request,'blog/about.html')

@login_required
def catogaries(request):
	y= quiz.objects.all().values('catogaries')
	x=list(y)
	a=[]
	for i in x:
		a.append(i['catogaries'])
	z=set(a)
	images=[]
	for i in z:
		image= Test.objects.filter(catogaries=i).values('Quiz_cover')
		print(list(image))
		print("//////////////////////////////////////////////")
	context={
	'quizs' :z,
	}
	return render(request,'blog/quiz_catlog.html',context)

@login_required
def quiz_page(request,cat):
	try:
		x=quiz.objects.filter(catogaries=cat)
	except:
		messages.success(request,f'Category not selected.')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	context1={
	 'quizs':x,
	 'totalq':len(x),
	 'category':cat,
	}
	return render(request,'blog/quiz_page.html',context1)

@login_required
def quiz_page_result(request):
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
	# print(score,total,eff)
	attempts=Attempts(qAttempter=request.user,q_name=datas['category'][0],totalQue=datas['length'][0], attemptedQue=total, 
	correct=score,accuracy=eff)
	attempts.save()
	return render(request,'blog/result.html',context)

@login_required
def questionUpload(request):
	return render(request,'blog/Questionupload.html')

@login_required
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

@login_required
def quiz_upload_cat(request):
	return render(request,'blog/quiz_upload_cat.html')

@login_required
def quiz_upload(request):
	global quizList
	if(request.method=="POST"):
		Category=request.POST.get("Category")
		Image=request.FILES["image"]
		quizList.append([Category,Image])
	print(quizList)
	return render(request,'blog/quiz_upload.html')

@login_required
def add_quiz_question(request):
	global quizList
	global testId
	if(request.method=="POST"):
		Question=request.POST.get("Question")
		Option1=request.POST.get("option")
		Option2=request.POST.get("option1")
		Option3=request.POST.get("option2")
		Option4=request.POST.get("option3")
		Answer=request.POST.get("Answer")
		Button=request.POST.get("Submit")
		if(Button=='Add'):
			quizList.append([Question,Option1,Option2,Option3,Option4,Answer])
			messages.success(request,"Question added Successfully.")
			return render(request,'blog/quiz_upload.html')
		else:
			testId+=1
			quizList.append([Question,Option1,Option2,Option3,Option4,Answer])
			for i in range(1,len(quizList)):
				location= "media\QuizCover\%s" %quizList[0][1]
				Imagefile = open(location)
				ques=Test(testId=testId,Quiz_cover=Imagefile,question=quizList[i][0],option1=quizList[i][1],option2=quizList[i][2],
				option3=quizList[i][3],option4=quizList[i][4],answer=quizList[i][4],catogaries=quizList[0][0],
				student=request.user)
				ques.save()
			messages.success(request,"Quiz submitted Successfully.")
			print(quizList)
			quizList=[]
			return render(request,'blog/quiz_upload_cat.html')