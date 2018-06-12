from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from course.forms import CourseForm
from course.models import Course

def course_list(request):
	courses = Course.objects.all()
	data = {}
	data['object_list'] = courses
	return render(request, 'course/list.html', data)

def course_details(request, pk):
	course = Course.objects.get(pk=pk)
	return render(request, 'course/detail.html', {'course':course})

def course_new(request):
	if request.method == "POST":
		form = CourseForm(request.POST)
		if form.is_valid():
			course = form.save(commit=False)
			course.save()	
			return redirect('course_details', pk=course.pk)
	else:
		form = CourseForm()
	return render(request, 'course/new.html', {'form':form})

def course_edit(request, pk):
	course = Course.objects.get(pk=pk)
	form = CourseForm(instance=course)
	
	if request.method == "POST":
		if form.is_valid():
			course = form.save(commit=False)
			course.save()
			return redirect('course_details', pk=course.pk)
		else:
			form = CourseForm()
	context = {'form' : form, 'course' : course}
	return render(request, 'course/new.html', context)

def course_remove(request, pk):
	course = Course.objects.get(pk=pk)
	course.delete()
	return redirect('course_list')