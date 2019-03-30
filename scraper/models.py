from django.db import models
from django import forms
from users.models import CustomUser
# Create your models here.


class ScrapingProcess(models.Model):
    #custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    website_lists = models.TextField(blank=True)
    file_source = models.FileField(blank=True, default="settings.MEDIA_ROOT/uploads/urls_backup.jpg", upload_to='uploads/')
    #file_source = "" #file_source not needed, will be converted into website_lists string 
    