from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateFrom

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

	context = {
	'u_form': u_form,
	'p_form':p_form
	}
	return render(request,'user/profile.html',context)