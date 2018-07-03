from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from course.models import Course, List, Summary, Link, Teacher, Post, Comment

class TeacherForm(forms.ModelForm):
	name = forms.CharField(max_length=100)

	class Meta:
		model = Teacher
		fields = ['name']

class CourseForm(forms.ModelForm):
	name = forms.CharField(max_length=100)
	code = forms.CharField(max_length=7)
	teachers = forms.ModelMultipleChoiceField(Teacher.objects.all())

	class Meta:
		model = Course
		fields = ['name', 'code','teachers']

class ListForm(forms.ModelForm):
	name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':'name-list'}))
	file = forms.FileField()
	tags = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':'tags-list'}))

	def __init__(self, course, *args, **kwargs):
		super(ListForm, self).__init__(*args, **kwargs)
		self.fields['teacher'] = forms.ModelChoiceField(queryset=Teacher.objects.filter(pk__in=course.teachers.all()))

	class Meta:
		model = List
		fields = ['name', 'file', 'tags', 'teacher']


class SummaryForm(forms.ModelForm):
	name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':'name-summary'}))
	file = forms.FileField()
	tags = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':'tags-summary'}))

	def __init__(self, course, *args, **kwargs):
		super(SummaryForm, self).__init__(*args, **kwargs)
		self.fields['teacher'] = forms.ModelChoiceField(queryset=Teacher.objects.filter(pk__in=course.teachers.all()))

	class Meta:
		model = Summary
		fields = ['name', 'file', 'tags', 'teacher']

class LinkForm(forms.ModelForm):
	name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':'name-link'}))
	link = forms.URLField(widget=forms.TextInput(attrs={'id':'link'}))
	tags = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':'tags-link'}))

	def __init__(self, course, *args, **kwargs):
		super(LinkForm, self).__init__(*args, **kwargs)
		self.fields['teacher'] = forms.ModelChoiceField(queryset=Teacher.objects.filter(pk__in=course.teachers.all()))

	class Meta:
		model = Link
		fields = ['name', 'link', 'tags', 'teacher']

class PostForm(forms.ModelForm):
	title = forms.CharField(label='Dúvida', max_length=100, widget=forms.TextInput(attrs={'id':'title-post'}))
	text = forms.CharField(label='Descrição', widget=forms.Textarea(attrs={'class':'materialize-textarea', 'id':'content-post'}))
	tags = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':'tags-post'}))

	class Meta:
		model = Post
		fields = ['title', 'text', 'tags']

class CommentForm(forms.ModelForm):
	text = forms.CharField(label='Comentário', widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))

	class Meta:
		model = Comment
		fields = ['text']