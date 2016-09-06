from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'views')# this list is what will show up in the admin site

admin.site.register(Post, PostAdmin)