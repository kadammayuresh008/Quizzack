from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateFrom
from blog.models import Attempts
from user.models import Profile
from django.contrib.auth.models import User

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Your account has been created! You are now able to login.')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request,'user/register.html',{'form':form})


@login_required
def profile(request):

	u_form = UserUpdateForm()
	p_form = ProfileUpdateFrom()

	if request.method == "POST":
		u_form = UserUpdateForm(request.POST)
		p_form = ProfileUpdateFrom(request.POST)
		if u_form.is_valid():
			data = u_form.cleaned_data
			User.objects.filter(username=request.user).update(username=data['username'], email=data['email'])
		if p_form.is_valid():
			data1 = p_form.cleaned_data
			Profile.objects.filter(user=request.user).update(image=data1['image'])
		# user.username = data['username']
		# user.email = data['email']
		# user.save()
		# newprofile= Profile(user=)


	a=Attempts.objects.filter(qAttempter=request.user).order_by('attemptedtime')
	if(len(a)>5):
		attempts=a[len(a)-5:]
	else:
		attempts=a
	context = {
	'u_form': u_form,
	'p_form':p_form,
	'attempts':attempts,
	'length':len(attempts)
	}
	return render(request,'user/profile.html',context)


