from django.contrib import admin
from .models import Hiretuber
# Register your models here.

class HtAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'email', 'created_date')
    list_display_links = ('email', 'first_name', 'id')

admin.site.register(Hiretuber, HtAdmin)