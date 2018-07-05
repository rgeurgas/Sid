from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	birth_date = forms.DateField(widget=forms.DateInput(attrs={'id':'birthdate', 'class':'datepicker'}))
	university = forms.CharField(max_length=50)
	bio = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'id':'id_bio', 'class':'materialize-textarea'}))
	email = forms.EmailField(max_length=254, help_text='Required. Please insert a valid email', widget=forms.EmailInput(attrs={'class':'validate'}))

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 
				  'university', 'bio', 'birth_date', 'password1', 'password2']

class EditarForm(forms.ModelForm):
	birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
	#COLOCAR DATEPICKER!!!
	university = forms.CharField(max_length=50)
	bio = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'id':'id_bio'}))
	image = forms.ImageField()

	class Meta:
		model = User
		fields = ['university', 'bio', 'birth_date', 'image']
