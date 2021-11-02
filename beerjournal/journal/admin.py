from django.contrib import admin

# Register your models here.
from .models import Beer, Entry

admin.site.register(Beer)
admin.site.register(Entry)