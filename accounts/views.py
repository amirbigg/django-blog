from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login


def user_login(request):
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('blog:all_articles')
	else:
		form = UserLoginForm()
	return render(request, 'accounts/login.html', {'form':form})