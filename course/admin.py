from django.contrib import admin

from course.models import Course, Link, List, Summary, Teacher

class LinkInline(admin.StackedInline):
	model = Link

class LinkAdmin(admin.ModelAdmin):
	fieldset = [
		(None, {'fields':['name']}),
		(None, {'fields':['description']}),
		(None, {'fields':['links']}),
	]

class ListInline(admin.StackedInline):
	model = List

class ListAdmin(admin.ModelAdmin):
	fieldset = [
		(None, {'fields':['name']}),
		(None, {'fields':['file']}),
	]

class SummaryInline(admin.StackedInline):
	model = Summary

class SummaryAdmin(admin.ModelAdmin):
	fieldset = [
		(None, {'fields':['name']}),
		(None, {'fields':['file']}),
	]

class CourseAdmin(admin.ModelAdmin):
	fieldset = [
		(None, {'fields':['name']}),
		(None, {'fields':['code']}),
	]
	inlines = [
		LinkInline,
		ListInline,
		SummaryInline,
	]

class TeacherAdmin(admin.ModelAdmin):
	fieldset = [
		(None, {'fields':['name']}),
	]


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(Summary, SummaryAdmin)
admin.site.register(Course, CourseAdmin)