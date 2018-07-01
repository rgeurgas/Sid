import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from course.forms import CourseForm, LinkForm, ListForm, SummaryForm
from course.models import Course, Link, List, Summary
from registration.models import Profile


def home(request):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)
		
		sub_courses = profile.courses.all()

		activities = []
		for course in sub_courses:
			for l in course.link.all():
				activities.append(l)
			for l in course.list.all():
				activities.append(l)
			for s in course.summary.all():
				activities.append(s)

		activities.sort(key = lambda x: x.date, reverse=True)

		context = {
			'courses': sub_courses,
			'activities': activities[:10]
		}
		
		return render(request, 'course/home.html', context)

	return render(request, 'course/home_logged_out.html')

def course_list(request):
	courses = Course.objects.all()
	data = {}
	data['object_list'] = courses
	return render(request, 'course/list.html', data)

def course_details(request, pk):
	course = Course.objects.get(pk=pk)

	if 'add_list' in request.POST:
		listForm = ListForm(request.POST, request.FILES)
		if listForm.is_valid():
			list_new = listForm.save(commit=False)
			list_new.course = course
			list_new.user = request.user
			list_new.tags.set(form.cleaned_data['tags'])
			list_new.save()
	else:
		listForm = ListForm()
	
	if 'add_link' in request.POST:
		linkForm = LinkForm(request.POST)
		if form.is_valid():
			link = linkForm.save(commit=False)
			link.course = course
			link.user = request.user
			link.save()
	else:
		linkForm = LinkForm()

	if 'add_summary' in request.POST:
		summaryForm = SummaryForm(request.POST, request.FILES)
		if summaryForm.is_valid():
			summary = summaryForm.save(commit=False)
			summary.course = course
			summary.user = request.user
			summary.tags.set(summaryForm.cleaned_data['tags'])
			summary.save()
	else:
		summaryForm = SummaryForm()

	context = {}
	
	return render(request, 'course/course_single.html', context)

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
	
	if request.method == "POST" and form.is_valid():
		course = form.save(commit=False)
		course.save()
		return redirect('course_details', pk=course.pk)
	
	context = {'form': form, 'course': course}
	return render(request, 'course/new.html', context)

def course_remove(request, pk):
	course = Course.objects.get(pk=pk)
	course.delete()
	return redirect('course_list')

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
	
	if request.method == "POST" and form.is_valid():
		link = form.save(commit=False)
		link.save()
		return redirect('link_detail', pk=link.pk)

	context = {'form': form, 'link': link}
	return render(request, 'course/new.html', context)

def link_remove(request, pk):
	link = Link.objects.get(pk=pk)
	pk = link.course
	link.delete()
	return redirect('course_details', pk)

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

	if request.method == "POST" and form.is_valid():
		list_c = form.save(commit=False)
		list_c.save()
		return redirect('list_detail', pk=list_c.pk)

	context = {'form': form, 'list': list_c}
	return render(request, 'course/new.html', context)

def list_remove(request, pk):
	list_c = List.objects.get(pk=pk)
	pk = list_c.course
	list_c.delete()
	return redirect('course_details', pk)

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
	if request.method == "POST" and form.is_valid():
		summary = form.save(commit=False)
		summary.save()
		return redirect('summary_detail', pk=summary.pk)
	context = {'form': form, 'summary': summary}
	return render(request, 'course/new.html', context)

def summary_remove(request, pk):
	summary = Summary.objects.get(pk=pk)
	pk = summary.course
	summary.delete()
	return redirect('course_details', pk)

def download(request, path):
	file_path = os.path.join(settings.MEDIA_ROOT, path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as f:
			response = HttpResponse(f.read(), content_type='application/force-download')
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
