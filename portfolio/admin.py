from django.contrib import admin
#from .models import Blogs
#from .models import Comment
from .models import Contacts
from .import models




# Register your models here.
admin.site.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
