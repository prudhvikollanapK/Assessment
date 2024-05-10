from django.contrib import admin
from .models import *

class AccountModel(admin.ModelAdmin):
    list_display=("email","account_id","account_name","app_secret_token","website")

admin.site.register(Account, AccountModel)

class DestinationModel(admin.ModelAdmin):
    list_display=("account","url","http_method","headers")

admin.site.register(Destination, DestinationModel)