from django.contrib import admin

from course.models import Course

class CourseAdmin(admin.ModelAdmin):
	fieldset = [
		(None, {'fields':['name']}),
		(None, {'fields':['code']}),
	]

admin.site.register(Course, CourseAdmin)