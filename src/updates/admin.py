from django.contrib import admin

from .models import Post, Comment, Hashtag

class PostAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Post._meta.fields]


class CommentAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Comment._meta.fields]


class HashtagAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Hashtag._meta.fields]


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Hashtag, HashtagAdmin)
