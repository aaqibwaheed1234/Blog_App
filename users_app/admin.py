from django.contrib import admin
from .models import Post, Comment
# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'intro', 'body', 'created_at', 'image']

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'body']

admin.site.register(Post,PostsAdmin)
admin.site.register(Comment,CommentsAdmin)