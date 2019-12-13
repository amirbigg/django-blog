from django.shortcuts import render
from .forms import UserLoginForm


def user_login(request):
	form = UserLoginForm()
	return render(request, 'accounts/login.html', {'form':form})