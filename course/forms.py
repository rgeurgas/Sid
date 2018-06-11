from django import forms

from course.models import Course, List, Summary, Link

class CourseForm(forms.ModelForm):
	name = forms.CharField(max_length=100)
	code = forms.CharField(max_length=8)
	class Meta:
		model = Course
		fields = ['name', 'code']

class ListForm(forms.ModelForm):
	name = forms.CharField(max_length=100)
	teacher = forms.CharField(max_length=100)
	# tags = forms.CharField(max_length=100)
	# course = forms.CharField(max_length=100)
	class Meta:
		model = List
		fields = ['name', 'teacher', 'tags', 'course']

class SummaryForm(forms.ModelForm):
	class Meta:
		model = Summary
		fields = ['name', 'teacher', 'tags', 'course']

class LinkForm(forms.ModelForm):
	class Meta:
		model = Link
		fields = ['name', 'description', 'link', 'teacher', 'tags', 'course']
