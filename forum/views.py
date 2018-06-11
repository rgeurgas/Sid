from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone

from forum.models import Post, Comment

class forumListView(ListView):
	model = Post
	paginate_by = 100  # if pagination is desired

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context
