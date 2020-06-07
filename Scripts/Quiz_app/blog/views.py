from django.shortcuts import render
from .models import quiz

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
		x=quiz.objects.filter(catogaries=datas['que'][0])
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