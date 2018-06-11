from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from forum.models import Post, Comment

def post_list(request):
	posts =  Post.objects.all()
	data = {}
	data['object_list'] = posts
	return render(request, 'forum/post_list.html', data)

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'forum/post.html', {'post':post})
