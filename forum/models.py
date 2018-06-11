from django.db import models

class Post(models.Model):
	user = models.CharField(max_length=50)
	title = models.CharField(max_length=100)
	text = models.TextField()
	date = models.DateTimeField('date published')
	#file = 
	#tags =

	def __str__(self):
		return self.title

class Comment(models.Model):
	user = models.CharField(max_length=50) # obs: depois vai ter um foreign key, só to usando assim p testar, ehnois
	text = models.TextField()
	#file
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')

	def __str__(self):
		return self.text

