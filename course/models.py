from django.db import models

def user_directory_path(filename):
    return 'uploads/%Y/%m/%d'

class Teacher(models.Model):
	name = models.CharField(max_length=100, null=False)

	def __str__(self):
		return self.name

class Course(models.Model):
	name = models.CharField(max_length=100, null=False)
	code = models.CharField(max_length=7, null=False, unique=True)
	teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, related_name='course')

	def __str__(self):
		return "{}-{}".format(self.code, self.name)

class Tag(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return "{}".format(self.name)

class List(models.Model):
	name = models.CharField(max_length=100, null=False)
	file = models.FileField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)
	tags = models.ManyToManyField(Tag, blank=True)
	course = models.ForeignKey('Course', on_delete=models.CASCADE, null=False, related_name='list')

	def __str__(self):
		return "{} --> {}".format(self.name, self.file)

class Summary(models.Model):
	name = models.CharField(max_length=100, null=False)
	file = models.FileField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)
	tags = models.ManyToManyField(Tag, blank=True)
	course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='summary')
	
	def __str__(self):
		return "{} --> {}".format(self.name, self.file)

class Link(models.Model):
	name = models.CharField(max_length=100, null=False)
	description = models.TextField(null=True, blank=True)
	link = models.URLField(null=False)
	tags = models.ManyToManyField(Tag, blank=True)
	course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='link')

	def __str__(self):
		return "{} --> {}".format(self.name, self.link)
