from django import forms

from course.models import Course, List, Summary, Link, Tag

class CourseForm(forms.ModelForm):
	name = forms.CharField(max_length=100)
	code = forms.CharField(max_length=7)
	
	class Meta:
		model = Course
		fields = ['name', 'code']

class ListForm(forms.ModelForm):
	name = forms.CharField(max_length=100)
	teacher = forms.CharField(max_length=100)
	file = forms.FileField()
	tags = forms.ModelMultipleChoiceField(Tag.objects.all())
	course = forms.ModelChoiceField(Course.objects.all())
	
	class Meta:
		model = List
		fields = ['name', 'teacher', 'file', 'tags', 'course']

class SummaryForm(forms.ModelForm):
	name = forms.CharField(max_length=100)
	teacher = forms.CharField(max_length=100)
	file = forms.FileField()
	tags = forms.ModelMultipleChoiceField(Tag.objects.all())
	course = forms.ModelChoiceField(Course.objects.all())
	
	class Meta:
		model = Summary
		fields = ['name', 'teacher', 'file', 'tags', 'course']

class LinkForm(forms.ModelForm):
	name = forms.CharField(max_length=100)
	description = forms.CharField(widget=forms.Textarea)
	link = forms.URLField()
	teacher = forms.CharField(max_length=100)
	tags = forms.ModelMultipleChoiceField(Tag.objects.all())
	course = forms.ModelChoiceField(Course.objects.all())

	class Meta:
		model = Link
		fields = ['name', 'description', 'link', 'teacher', 'tags', 'course']
