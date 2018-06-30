from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
	university = forms.CharField(max_length=50)
	email = forms.EmailField(max_length=254, help_text='Required. Please insert a valid email')

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 
				  'university', 'birth_date', 'password1', 'password2',]
