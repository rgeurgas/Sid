from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def user_directory_path(filename):
    return 'uploads/%Y/%m/%d'

class Teacher(models.Model):
	name = models.CharField(max_length=100, null=False)

	def __str__(self):
		return self.name

class Course(models.Model):
	name = models.CharField(max_length=100, null=False)
	code = models.CharField(max_length=7, null=False, unique=True)
	teachers = models.ManyToManyField(Teacher, blank=True)

	def __str__(self):
		return "{}-{}".format(self.code, self.name)

class List(models.Model):
	name = models.CharField(max_length=100, null=False)
	file = models.FileField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	tags = models.CharField(max_length=100)
	course = models.ForeignKey('Course', on_delete=models.CASCADE, null=False, related_name='list')
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='list')
	teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, blank=True, related_name='list')

	def __str__(self):
		return "{} --> {}".format(self.name, self.file)

class Summary(models.Model):
	name = models.CharField(max_length=100, null=False)
	file = models.FileField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	tags = models.CharField(max_length=100)
	course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='summary')
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='summary')
	teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, blank=True, related_name='summary')
	
	def __str__(self):
		return "{} --> {}".format(self.name, self.file)

class Link(models.Model):
	name = models.CharField(max_length=100, null=False)
	link = models.URLField(null=False)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	tags = models.CharField(max_length=100)
	course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='link')
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='link')
	teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, blank=True, related_name='link')

	def __str__(self):
		return "{} --> {}".format(self.name, self.link)

class Post(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	date = models.DateTimeField(auto_now_add=True, blank=True)
	tags = models.CharField(max_length=100)
	document = models.FileField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='post')
	course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True, related_name='post')

	def __str__(self):
		return self.title

class Comment(models.Model):
	text = models.TextField()
	document = models.FileField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='comment')
	date = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.text
