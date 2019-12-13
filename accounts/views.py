from django.shortcuts import render
from .forms import UserLoginForm


def user_login(request):
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			print('+'*80)
			print(username, password)
	else:
		form = UserLoginForm()
	return render(request, 'accounts/login.html', {'form':form})