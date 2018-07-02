from django import forms

from django.contrib.auth.models import User
from course.models import Course, List, Summary, Link, Teacher

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
	name = forms.CharField(max_length=100)
	file = forms.FileField()
	tags = forms.CharField(max_length=100)
	teacher = forms.ModelChoiceField(Teacher.objects.all())
	
	class Meta:
		model = List
		fields = ['name', 'file', 'tags', 'teacher']


class SummaryForm(forms.ModelForm):
	name = forms.CharField(max_length=100)
	file = forms.FileField()
	tags = forms.CharField(max_length=100)
	teacher = forms.ModelChoiceField(Teacher.objects.all())
	
	class Meta:
		model = Summary
		fields = ['name', 'file', 'tags', 'teacher']

class LinkForm(forms.ModelForm):
	name = forms.CharField(max_length=100)
	link = forms.URLField()
	tags = forms.CharField(max_length=100)
	teacher = forms.ModelChoiceField(Teacher.objects.all())

	class Meta:
		model = Link
		fields = ['name', 'link', 'tags', 'teacher']
