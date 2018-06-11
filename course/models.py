from django.db import models

class Course(models.Model):
	name = models.CharField(max_length=100, null=False)
	code = models.CharField(max_length=8, null=False, unique=True)

class Tag(models.Model):
	name = models.CharField(max_length=50)

class File(models.Model):
	name = models.CharField(max_length=100)
	file = models.FileField(upload_to='uploads/{instance.user.id}/{filename}')
	ownerList = models.ForeignKey('List', on_delete=models.CASCADE)
	ownerSummary = models.ForeignKey('Summary', on_delete=models.CASCADE)

class List(models.Model):
	name = models.CharField(max_length=100, null=False)
	teacher = models.CharField(max_length=100)
	tags = models.ManyToManyField(Tag)
	course = models.ForeignKey('Course', on_delete=models.CASCADE)

class Summary(models.Model):
	name = models.CharField(max_length=100, null=False)
	teacher = models.CharField(max_length=100)
	tags = models.ManyToManyField(Tag)
	course = models.ForeignKey('Course', on_delete=models.CASCADE)

class Link(models.Model):
	name = models.CharField(max_length=100, null=False)
	description = models.TextField()
	link = models.CharField(max_length=100)
	teacher = models.CharField(max_length=100)
	tags = models.ManyToManyField(Tag)
	course = models.ForeignKey('Course', on_delete=models.CASCADE)
