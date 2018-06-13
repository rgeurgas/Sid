from django.contrib import admin
from forum.models import Post, Comment, Tag

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['user', 'title', 'text']}),
        ('Date information', {'fields': ['date'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
#admin.site.register(Comment)
