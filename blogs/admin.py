from django.contrib import admin

from .models import Author, Post

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_date']
