from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
	#COLOCAR DATEPICKER!!!
	university = forms.CharField(max_length=50)
	bio = forms.CharField(max_length=500)
	email = forms.EmailField(max_length=254, help_text='Required. Please insert a valid email')

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 
				  'university', 'bio', 'birth_date', 'password1', 'password2']

class EditarForm(UserCreationForm):
	first_name = forms.CharField(max_length=150)
	last_name = forms.CharField(max_length=150)
	birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
	#COLOCAR DATEPICKER!!!
	university = forms.CharField(max_length=50)
	bio = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'id':'id_email'}))
	email = forms.EmailField(max_length=254, help_text='Required. Please insert a valid email')
	image = forms.ImageField()

	class Meta:
		model = User
		fields = ['university', 'bio', 'birth_date', 'image']
