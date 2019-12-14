from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
	username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your username'}))
	password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Your password'}))


class UserRegistrationForm(forms.Form):
	username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your username'}))
	email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your Email'}))
	password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your password'}))

	def clean_email(self):
		email = self.cleaned_data['email']
		user = User.objects.filter(email=email)
		if user.exists():
			raise forms.ValidationError('This email already exists')
		return email