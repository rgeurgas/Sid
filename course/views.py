from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from course.forms import CourseForm, LinkForm, ListForm, SummaryForm
from course.models import Course, Link, List, Summary

def course_list(request):
	courses = Course.objects.all()
	data = {}
	data['object_list'] = courses
	return render(request, 'course/list.html', data)

def course_details(request, pk):
	course = Course.objects.get(pk=pk)
	context = {'course':course}	
	return render(request, 'course/detail.html', context)

def course_new(request):
	if request.method == "POST":
		form = CourseForm(request.POST)		
		if form.is_valid():
			course = form.save(commit=False)
			course.save()	
			return redirect('course_details', pk=course.pk)
	else:
		form = CourseForm()

	context = {'form': form}
	return render(request, 'course/new.html', context)

def course_edit(request, pk):
	course = Course.objects.get(pk=pk)
	form = CourseForm(instance=course)
	
	if request.method == "POST":
		if form.is_valid():
			course = course_form.save(commit=False)
			course.save()
			handle_uploaded_file(request.FILES['file'])
			return redirect('course_details', pk=course.pk)
		else:
			form = CourseForm()

	context = {'form': form, 'course': course}
	return render(request, 'course/new.html', context)

def course_remove(request, pk):
	course = Course.objects.get(pk=pk)
	course.delete()
	return redirect('course_list')

def link_add(request):
	if request.method == "POST":
		form = LinkForm(request.POST)
		if form.is_valid():
			link = form.save(commit=False)
			link.save()
			return redirect('course_list')
	else:
		form = LinkForm()
	context = {'form' : form}
	return render(request, 'course/new.html', context)

def list_add(request):
	if request.method == "POST":
		form = ListForm(request.POST, request.FILES)
		if form.is_valid():
			list_new = form.save(commit=False)
			list_new.save()

			return redirect('course_list')
	else:
		form = ListForm()
	context = {'form' : form}
	
	return render(request, 'course/new.html', context)

def summary_add(request):
	if request.method == "POST":
		form = SummaryForm(request.POST)
		if form.is_valid():
			summary = form.save(commit=False)
			summary.save()
			return redirect('course_list')
	else:
		form = SummaryForm()
	context = {'form' : form}
	return render(request, 'course/new.html', context)
