from django.contrib import admin

from course.models import Course, Link, List, Summary, Post, Comment, Teacher

class LinkInline(admin.StackedInline):
	model = Link

class LinkAdmin(admin.ModelAdmin):
	fieldset = [
		(None, {'fields':['name', 'description', 'links']}),
	]

class ListInline(admin.StackedInline):
	model = List

class ListAdmin(admin.ModelAdmin):
	fieldset = [
		(None, {'fields':['name', 'file']}),
	]

class SummaryInline(admin.StackedInline):
	model = Summary

class SummaryAdmin(admin.ModelAdmin):
	fieldset = [
		(None, {'fields':['name', 'file']}),
	]

class CourseAdmin(admin.ModelAdmin):
	fieldset = [
		(None, {'fields':['name', 'code']}),
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

class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'text', 'document']}),
    ]

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'title', 'text', 'tags', 'document']}),
    ]
    inlines = [CommentInline]

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(Summary, SummaryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
