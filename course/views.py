from django.shortcuts import render, redirect

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

def link_list(request):
	links = Link.objects.all()
	data = {}
	data['object_list'] = links
	return render(request, 'course/list.html', data)

def link_detail(request, pk):
	link = Link.objects.get(pk=pk)
	context = {'link':link}
	return render(request, 'course/detail.html', context)

def link_edit(request, pk):
	link = Link.objects.get(pk=pk)
	form = LinkForm(instance=link)
	
	if request.method == "POST":
		if form.is_valid():
			link = form.save(commit=False)
			link.save()
			return redirect('link_detail', pk=pk)
		else:
			form = LinkForm()
	context = {'form': form, 'link': link}
	return render(request, 'course/new.html', context)

def link_remove(request, pk):
	link = Link.objects.get(pk=pk)
	pk = link.course
	link.delete()
	return redirect('course_detail', pk)

def list_add(request):
	if request.method == "POST":
		form = ListForm(request.POST, request.FILES)
		if form.is_valid():
			list_new = form.save(commit=False)
			list_new.save()
			list_new.tags.set(form.cleaned_data['tags'])

			return redirect('course_list')
	else:
		form = ListForm()
	context = {'form' : form}
	
	return render(request, 'course/new.html', context)

def list_list(request):
	lists = List.objects.all()
	data = {}
	data['object_list'] = lists
	return render(request, 'course/list.html', data)

def list_detail(request, pk):
	list_c = List.objects.get(pk=pk)
	context = {'list':list_c}
	return render(request, 'course/detail.html', context)

def list_edit(request, pk):
	list_c = List.objects.get(pk=pk)
	form = ListForm(instance=list_c)

	if request.method == "POST":
		if form.is_valid():
			list_c = form.save(commit=False)
			list_c.save()
			return redirect('list_detail', pk=pk)
	else:
		form = LinkForm()
	context = {'form': form, 'list': list_c}
	return render(request, 'course/new.html', context)

def list_remove(request, pk):
	list_c = List.objects.get(pk=pk)
	pk = list_c.course
	list_c.delete()
	return redirect('course_detail', pk)

def summary_add(request):
	if request.method == "POST":
		form = SummaryForm(request.POST, request.FILES)
		if form.is_valid():
			summary = form.save(commit=False)
			summary.save()
			summary.tags.set(form.cleaned_data['tags'])

			return redirect('course_list')
		else:
			form = SummaryForm()
	context = {'form' : form}
	return render(request, 'course/new.html', context)

def summary_list(request):
	summaries = Summary.objects.all()
	data = {}
	data['object_list'] = summaries
	return render(request, 'course/list.html', data)

def summary_detail(request, pk):
	summary = Summary.objects.get(pk=pk)
	context = {'summary':summary}
	return render(request, 'course/detail.html', context)

def summary_edit(request, pk):
	summary = Summary.objects.get(pk=pk)
	form = SummaryForm(instance=summary)
	if request.method == "POST":
		if form.is_valid():
			summary = form.save(commit=False)
			summary.save()
			return redirect('summary_detail', pk=pk)
		else:
			form = LinkForm()
	context = {'form': form, 'summary': summary}
	return render(request, 'course/new.html', context)

def summary_remove(request, pk):
	summary = Summary.objects.get(pk=pk)
	pk = summary.course
	summary.delete()
	return redirect('course_detail', pk)
