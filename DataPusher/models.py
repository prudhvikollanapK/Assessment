from django.db import models

class Account(models.Model):
    email = models.EmailField(unique=True)
    account_id = models.CharField(max_length=100, unique=True)
    account_name = models.CharField(max_length=100)
    app_secret_token = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)

class Destination(models.Model):
    account = models.ForeignKey(Account, related_name='destinations', on_delete=models.CASCADE)
    url = models.URLField()
    http_method = models.CharField(max_length=10)
    headers = models.JSONField()