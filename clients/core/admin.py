from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    # fields = ['name', 'last_name', 'age', 'salary']
    list_display = ['name', 'last_name', 'age', 'salary']
    list_filter = ['name', 'last_name', 'age', 'salary']
    search_fields = ['last_name', 'age']

admin.site.register(Client, ClientAdmin)
# admin.site.register(Client)