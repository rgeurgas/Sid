from django import forms
from django.utils import timezone

from forum.models import Post, Comment

class PostForm(forms.ModelForm):
	user = forms.CharField(label='Usuário', max_length=50)
	title = forms.CharField(label='Dúvida', max_length=100)
	text = forms.CharField(label='Descrição', widget=forms.Textarea)
	#date = forms.DateTimeField('date published')

	class Meta:
		model = Post
		fields = ['user', 'title', 'text', 'tags']

class CommentForm(forms.ModelForm):
	user = forms.CharField(label='Usuário', max_length=50)
	text = forms.CharField(label='Comentário', widget=forms.Textarea)

	class Meta:
		model = Comment
		fields = ['user', 'text']