from django.db import models
from django.utils import timezone

class Tag(models.Model):
	name = models.CharField(max_length=50)

class Post(models.Model):
	user = models.CharField(max_length=50)
	title = models.CharField(max_length=100)
	text = models.TextField()
	date = models.DateTimeField(auto_now_add=True, blank=True)
	tags = models.ManyToManyField(Tag)
	document = models.FileField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	user = models.CharField(max_length=50) # obs: depois vai ter um foreign key, só to usando assim p testar, ehnois
	text = models.TextField()
	document = models.FileField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')

	def __str__(self):
		return self.text

