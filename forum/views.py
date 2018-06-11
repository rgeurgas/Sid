from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from forum.models import Post, Comment
from forum.forms import PostForm

def post_list(request):
	posts =  Post.objects.all()
	data = {}
	data['object_list'] = posts
	return render(request, 'forum/post_list.html', data)

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'forum/post.html', {'post':post})

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)

		if form.is_valid():
			post = form.save(commit=False)
			post.save()	
			return redirect('forum/', pk=post.pk)
	else:
		form = PostForm()

	return render(request, 'forum/post_new.html', {'form':form})
