from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from forum.models import Post, Comment
from forum.forms import PostForm, CommentForm

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
			new_comment.save()	
			return redirect('post_detail', pk=post.pk)
	else:
		form = CommentForm()

	return render(request, 'forum/post.html', {'post':post, 'form':form})

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)

		if form.is_valid():
			post = form.save(commit=False)
			post.save()	
			return redirect('/forum/', pk=post.pk)
	else:
		form = PostForm()

	return render(request, 'forum/post_new.html', {'form':form})

def post_edit(request, pk=None):
	if pk:
		post = Post.objects.get(pk=pk)

	if request.method == 'POST' and form.is_valid():
		form = PostForm(request.POST or None, request.FILES, instance=post)
		form.save()	
		return redirect('/forum/', pk=post.pk)
	else:
		form = PostForm()

	return render(request, 'forum/post_new.html', {'form':form})


def post_remove(request, pk):
	post = Post.objects.get(pk=pk)
	post.delete()
	return redirect('post_list') 

def comment_remove(request, pk):	# obs: o pk equivale ao comment
	comment = Comment.objects.get(pk=pk)
	comment.delete()
	return redirect('post_detail', pk=comment.post.pk) 

