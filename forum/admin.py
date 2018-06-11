from django.contrib import admin
from forum.models import Post, Comment

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['date'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
#admin.site.register(Comment)
