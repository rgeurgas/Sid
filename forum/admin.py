# from django.contrib import admin
# from forum.models import Post, Comment

# class CommentAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,{'fields': ['user', 'text', 'document']}),
#     ]

# class CommentInline(admin.StackedInline):
#     model = Comment
#     extra = 0

# class PostAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['user', 'title', 'text', 'tags', 'document']}),
#     ]
#     inlines = [CommentInline]

# admin.site.register(Post, PostAdmin)
# admin.site.register(Comment, CommentAdmin)
