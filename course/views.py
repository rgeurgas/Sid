import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

from course.models import Course, Link, List, Summary, Post, Comment, Teacher
from course.forms import CourseForm, LinkForm, ListForm, SummaryForm, PostForm, CommentForm
from registration.models import Profile

def home(request):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)
		
		sub_courses = profile.courses.all()

		activities = []
		for course in sub_courses:
			for l in course.link.all()[:10]:
				activities.append({'obj': l, 'tipo': 'um link'})
			for l in course.list.all()[:10]:
				activities.append({'obj': l, 'tipo': 'uma lista'})
			for s in course.summary.all()[:10]:
				activities.append({'obj': s, 'tipo': 'um resumo'})

		activities.sort(key = lambda x: x['obj'].date, reverse=True)
		activities = activities[:10]

		context = {
			'courses': sub_courses,
			'activities': activities
		}
		
		return render(request, 'course/home.html', context)

	return redirect('login')

def course_search(request):
	query = request.GET.get('q')
	query_tags = query.split(' ')

	results = set()

	for tag in query_tags:
		for result in Course.objects.all().filter(name__icontains = tag):
			results.add(result)
		for result in Course.objects.all().filter(code__icontains = tag):
			results.add(result)
		for teacher in Teacher.objects.all().filter(name__icontains = tag):
			for result in Course.objects.all().filter(teachers=teacher.id):
				results.add(result)
	results = list(results)


	profile = Profile.objects.get(user=request.user)
	user_courses = profile.courses.all()

	context = {
		'search_courses': results,
		'user_courses': user_courses,
		'has_results': len(results) > 0,
		'has_user_courses': len(user_courses) > 0
	}

	return render(request, 'course/course_search.html', context)

def course_list(request):
	courses = Course.objects.all()
	data = {}
	data['object_list'] = courses
	return render(request, 'course/list.html', data)

def course_details(request, pk):
	course = Course.objects.get(pk=pk)

	if 'add_list' in request.POST:
		listForm = ListForm(course, request.POST, request.FILES)
		if listForm.is_valid():
			list_new = listForm.save(commit=False)
			list_new.course = course
			list_new.user = request.user
			list_new.save()
	else:
		listForm = ListForm(course)
	
	if 'add_link' in request.POST:
		linkForm = LinkForm(course, request.POST)
		if linkForm.is_valid():
			link = linkForm.save(commit=False)
			link.course = course
			link.user = request.user
			link.save()
	else:
		linkForm = LinkForm(course)

	if 'add_summary' in request.POST:
		summaryForm = SummaryForm(course, request.POST, request.FILES)
		if summaryForm.is_valid():
			summary = summaryForm.save(commit=False)
			summary.course = course
			summary.user = request.user
			summary.save()
	else:
		summaryForm = SummaryForm(course)

	if 'add_post' in request.POST:
		postForm = PostForm(request.POST)
		if postForm.is_valid():
			post = postForm.save(commit=False)
			post.course = course
			post.user = request.user
			post.save()
	else:
		postForm = PostForm()

	context = {'course':course, 'listForm':listForm,'linkForm':linkForm,
		 'summaryForm':summaryForm, 'postForm':postForm}
	
	return render(request, 'course/course_single.html', context)

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)

		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()	
			return redirect('/forum/', pk=post.pk)
	else:
		form = PostForm()

	return render(request, 'forum/post_new.html', {'form':form})


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

def post_list(request):
	posts =  Post.objects.all()
	data = {}
	data['object_list'] = posts
	return render(request, 'forum/post_list.html', data)

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)

	if request.method == 'POST':
		form = CommentForm(request.POST, request.FILES)

		if form.is_valid():
			new_comment = form.save(commit=False)
			new_comment.post = post
			new_comment.user = request.user
			new_comment.save()	
			return redirect('post_detail', pk=post.pk)
	else:
		form = CommentForm()

	return render(request, 'forum/post.html', {'post':post, 'form':form})

def post_edit(request, pk=None):
	post = Post.objects.get(pk=pk)
	form = PostForm(instance=post)

	if request.method == 'POST':
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('/forum/', pk=post.pk)
		else:
			form = PostForm()

	return render(request, 'forum/post_new.html', {'form':form, 'post':post})


def post_remove(request, pk):
	post = Post.objects.get(pk=pk)
	post.delete()
	return redirect('post_list') 

def comment_remove(request, pk):	# obs: o pk equivale ao comment
	comment = Comment.objects.get(pk=pk)
	comment.delete()
	return redirect('post_detail', pk=comment.post.pk) 

