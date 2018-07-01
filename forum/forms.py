from django import forms
from django.utils import timezone

from forum.models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
	#user = forms.ModelChoiceField(User.objects.all())
	title = forms.CharField(label='Dúvida', max_length=100)
	text = forms.CharField(label='Descrição', widget=forms.Textarea)
	#date = forms.DateTimeField('date published')

	class Meta:
		model = Post
		fields = ['title', 'text', 'tags']

class CommentForm(forms.ModelForm):
	#user = forms.ModelChoiceField(User.objects.all())
	text = forms.CharField(label='Comentário', widget=forms.Textarea)

	class Meta:
		model = Comment
		fields = ['text']