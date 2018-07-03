import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

from course.models import Course, Link, List, Summary, Post, Comment
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
			'profile': profile,
			'courses': sub_courses,
			'activities': activities
		}
		
		return render(request, 'course/home.html', context)

	return redirect('login')

def course_list(request):
	courses = Course.objects.all()
	data = {}
	data['object_list'] = courses
	
	if 'subscribe' in request.POST:
		profile = request.user.profile
		profile.courses 

	return render(request, 'course/list.html', data)

def course_details(request, pk):
	course = Course.objects.get(pk=pk)

	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)
		
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
	
	return redirect('login')

def link_list(request):
	links = Link.objects.all()
	data = {}
	data['object_list'] = links
	return render(request, 'course/list.html', data)

def link_detail(request, pk):
	link = Link.objects.get(pk=pk)
	context = {'link':link}
	return render(request, 'course/detail.html', context)

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

def post_list(request, course_pk):
	posts = Post.objects.all()
	course = Course.objects.get(pk=course_pk)

	posts = list(posts)
	posts.sort(key=lambda x: x.date, reverse=True)
	
	if request.method == 'POST':
		form = PostForm(request.POST)
		if 'add_post' in request.POST and form.is_valid():
			new_post = form.save(commit=False)
			new_post.user = request.user
			new_post.course = course
			new_post.save()
			return redirect('post_list', course_pk=course_pk)
	else:
		form = PostForm()
	print(form)
	data = {'form': form, 'posts': posts, 'course':course}
	
	return render(request, 'course/forum_list.html', data)

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	
	comments = list(post.comment.all())
	comments.sort(key=lambda x: x.date, reverse=False)

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if 'add_comment' in request.POST and form.is_valid():
			new_comment = form.save(commit=False)
			new_comment.post = post
			new_comment.user = request.user
			new_comment.save()	
			return redirect('post_detail', pk=post.pk)
	else:
		form = CommentForm()
	
	context = {'post':post, 'form':form, 'comments':comments}
	
	return render(request, 'course/forum_single.html', context)

def post_remove(request, pk):
	post = Post.objects.get(pk=pk)
	post.delete()
	return redirect('post_list') 

def comment_remove(request, pk):	# obs: o pk equivale ao comment
	comment = Comment.objects.get(pk=pk)
	comment.delete()
	return redirect('post_detail', pk=comment.post.pk) 

