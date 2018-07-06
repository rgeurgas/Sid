import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required

from course.models import Course, Link, List, Summary, Post, Comment, Teacher
from course.forms import CourseForm, LinkForm, ListForm, SummaryForm, PostForm, CommentForm
from registration.models import Profile

@login_required
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

@login_required
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

@login_required
def course_details(request, pk):
	course = Course.objects.get(pk=pk)

	if request.user.is_authenticated:
		profile = Profile.objects.get(user=request.user)

		if 'add_list' in request.POST and request.method == "POST":
			listForm = ListForm(course, request.POST, request.FILES)
			if listForm.is_valid():
				list_new = listForm.save(commit=False)
				list_new.course = course
				list_new.user = request.user
				list_new.save()
				return redirect('course_details', pk)
		else:
			listForm = ListForm(course)
		
		if 'add_link' in request.POST and request.method == "POST":
			linkForm = LinkForm(course, request.POST)
			if linkForm.is_valid():
				link = linkForm.save(commit=False)
				link.course = course
				link.user = request.user
				link.save()
				return redirect('course_details', pk)
		else:
			linkForm = LinkForm(course)

		if 'add_summary' in request.POST and request.method == "POST":
			summaryForm = SummaryForm(course, request.POST, request.FILES)
			if summaryForm.is_valid():
				summary = summaryForm.save(commit=False)
				summary.course = course
				summary.user = request.user
				summary.save()
				return redirect('course_details', pk)
		else:
			summaryForm = SummaryForm(course)
		
		if 'add_post' in request.POST:

			postForm = PostForm(request.POST)
			if postForm.is_valid():
				post = postForm.save(commit=False)
				post.course = course
				post.user = request.user
				post.save()
				return redirect('course_details', pk)
		else:
			postForm = PostForm()

		context = {'course':course, 'listForm':listForm,'linkForm':linkForm,
				   'summaryForm':summaryForm, 'postForm':postForm}

		return render(request, 'course/course_single.html', context)
	
	return redirect('login')

@login_required
def course_all_links(request, course_pk):
	course = Course.objects.get(pk=course_pk)
	
	if request.GET:
		query = request.GET.get('q')

		query_tags = query.split(' ')

		links = set()
		for query_tag in query_tags:
			for result in course.link.all().filter(name__icontains = query_tag):
				links.add(result)
			for result in course.link.all().filter(tags__icontains = query_tag):
				links.add(result)
		links = list(links)

		linkForm = LinkForm(course)
	elif request.POST:
		linkForm = LinkForm(course, request.POST)
		links = course.link.all()
		if linkForm.is_valid():
			link = linkForm.save(commit=False)
			link.course = course
			link.user = request.user
			link.save()
			return redirect('links_see_more', course_pk)
	else:
		linkForm = LinkForm(course)
		links = course.link.all()

	context = {
			'course': course,
			'links': links,
			'linkForm': linkForm,
	}

	return render(request, 'course/course_link_list.html', context)

@login_required
def course_all_lists(request, course_pk):
	course = Course.objects.get(pk=course_pk)
	
	if request.GET:
		query = request.GET.get('q')
		query_tags = query.split(' ')

		lists = set()
		for query_tag in query_tags:
			for result in course.list.all().filter(name__icontains = query_tag):
				lists.add(result)
			for result in course.list.all().filter(tags__icontains = query_tag):
				lists.add(result)
		lists = list(lists)

		listForm = ListForm(course)

	elif request.POST:
		listForm = ListForm(course, request.POST, request.FILES)
		lists = course.list.all()
		if listForm.is_valid():
			list_new = listForm.save(commit=False)
			list_new.course = course
			list_new.user = request.user
			list_new.save()
			return redirect('lists_see_more', course_pk)
	else:
		listForm = ListForm(course)
		lists = course.list.all()

	context = {
			'course': course,
			'lists': lists,
			'listForm': listForm,
	}

	return render(request, 'course/course_list_list.html', context)

@login_required
def course_all_summaries(request, course_pk):
	course = Course.objects.get(pk=course_pk)
	
	if request.GET:
		query = request.GET.get('q')
		query_tags = query.split(' ')

		summaries = set()
		for query_tag in query_tags:
			for result in course.summary.all().filter(name__icontains = query_tag):
				summaries.add(result)
			for result in course.summary.all().filter(tags__icontains = query_tag):
				summaries.add(result)
		summaries = list(summaries)

		summaryForm = SummaryForm(course)
	elif request.POST:
		summaryForm = SummaryForm(course, request.POST, request.FILES)
		summaries = course.summary.all()
		if summaryForm.is_valid():
			summary = summaryForm.save(commit=False)
			summary.course = course
			summary.user = request.user
			summary.save()
			return redirect('summaries_see_more', course_pk)
	else:
		summaryForm = SummaryForm(course)
		summaries = course.summary.all()

	context = {
			'course': course,
			'summaries': summaries,
			'summaryForm': summaryForm,
	}

	return render(request, 'course/course_summary_list.html', context)

@login_required
def course_sub(request, course_pk):
	profile = Profile.objects.get(user=request.user)
	profile.courses.add(course_pk)

	return redirect('course_details', pk=course_pk)

@login_required
def course_unsub(request, course_pk):
	profile = Profile.objects.get(user=request.user)
	profile.courses.remove(course_pk)

	return redirect('course_details', pk=course_pk)

@login_required
def link_remove(request, pk):
	link = Link.objects.get(pk=pk)
	pk = link.course.id
	
	if request.user.username == link.user.username:
		link.delete()
	
	return redirect('course_details', pk)

@login_required
def list_remove(request, pk):
	list_c = List.objects.get(pk=pk)
	pk = list_c.course.id
		
	if request.user.username == list_c.user.username:
		list_c.delete()
	
	return redirect('course_details', pk)

@login_required
def summary_remove(request, pk):
	summary = Summary.objects.get(pk=pk)
	pk = summary.course.id
	
	if request.user.username == summary.user.username:
		summary.delete()
	
	return redirect('course_details', pk)

@login_required
def download(request, path):
	file_path = os.path.join(settings.MEDIA_ROOT, path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as f:
			response = HttpResponse(f.read(), content_type='application/force-download')
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response

@login_required
def post_new(request, course_pk):
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

@login_required
def post_list(request, course_pk):
	posts = Post.objects.all()
	course = Course.objects.get(pk=course_pk)

	posts = list(posts)
	posts.sort(key=lambda x: x.date, reverse=True)
	
	if request.method == 'POST':
		postForm = PostForm(request.POST)
		if 'add_post' in request.POST and postForm.is_valid():
			new_post = postForm.save(commit=False)
			new_post.user = request.user
			new_post.course = course
			new_post.save()
			return redirect('post_list', course_pk=course_pk)
	else:
		postForm = PostForm()

	data = {'postForm': postForm, 'posts': posts, 'course':course}
	
	return render(request, 'course/forum_list.html', data)

@login_required
def post_detail(request, course_pk, pk):
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
			return redirect('post_detail', course_pk=course_pk, pk=post.pk)
	else:
		form = CommentForm()
	
	context = {'post':post, 'form':form, 'comments':comments}
	
	return render(request, 'course/forum_single.html', context)

@login_required
def post_remove(request, course_pk, pk):
	post = Post.objects.get(pk=pk)
	
	if request.user.username == post.user.username:
		post.delete()
	
	return redirect('post_list') 

@login_required
def comment_remove(request, course_pk, pk):	# obs: o pk equivale ao comment
	comment = Comment.objects.get(pk=pk)
	
	if request.user.username == comment.user.username:
		comment.delete()
	
	return redirect('post_detail', course_pk=comment.post.course.id, pk=comment.post.pk) 
