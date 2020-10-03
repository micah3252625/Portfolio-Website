from django.contrib import admin
from .models import Blogs
from .models import Comment
from .import models
from mptt.admin import MPTTModelAdmin



# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'author')

admin.site.register(Blogs, AuthorAdmin)

admin.site.register(models.Category)

admin.site.register(models.Comment, MPTTModelAdmin)
