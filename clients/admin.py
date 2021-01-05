from django.contrib import admin
from .models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'nick_name',
        'email',
        'password',
        'address',
        'city',
        'province',
        'country',
        'postal_code'
    ]