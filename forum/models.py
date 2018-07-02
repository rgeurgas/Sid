# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User

# from course.models import Course

# class Post(models.Model):
# 	title = models.CharField(max_length=100)
# 	text = models.TextField()
# 	date = models.DateTimeField(auto_now_add=True, blank=True)
# 	tags = models.CharField(max_length=100)
# 	document = models.FileField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)
# 	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='post')
# 	course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name='post')

# 	def __str__(self):
# 		return self.title

# class Comment(models.Model):
# 	text = models.TextField()
# 	document = models.FileField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)
# 	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
# 	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='comment')
# 	date = models.DateTimeField(auto_now_add=True, blank=True)

# 	def __str__(self):
# 		return self.text
