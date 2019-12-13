from django import forms


class UserLoginForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=50)