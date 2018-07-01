from django import forms

from course.models import Course, List, Summary, Link, Tag, Teacher

class TeacherForm(forms.ModelForm):
	name = forms.CharField(max_length=100)

	class Meta:
		model = Teacher
		fields = ['name']

class CourseForm(forms.ModelForm):
	name = forms.CharField(max_length=100)
	code = forms.CharField(max_length=7)
	teacher = forms.ModelChoiceField(Teacher.objects.all())

	class Meta:
		model = Course
		fields = ['name', 'code','teacher']

class ListForm(forms.ModelForm):
	name = forms.CharField(max_length=100)
	file = forms.FileField()
	tags = forms.ModelMultipleChoiceField(Tag.objects.all())
	
	class Meta:
		model = List
		fields = ['name', 'file', 'tags']

class SummaryForm(forms.ModelForm):
	name = forms.CharField(max_length=100)
	file = forms.FileField()
	tags = forms.ModelMultipleChoiceField(Tag.objects.all())
	
	class Meta:
		model = Summary
		fields = ['name', 'file', 'tags']

class LinkForm(forms.ModelForm):
	name = forms.CharField(max_length=100)
	description = forms.CharField(widget=forms.Textarea)
	link = forms.URLField()
	tags = forms.ModelMultipleChoiceField(Tag.objects.all())

	class Meta:
		model = Link
		fields = ['name', 'description', 'link', 'tags']
