from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("image", 'title', 'desc')
    search_fields = ['title']

admin.site.register(Post, PostAdmin)
