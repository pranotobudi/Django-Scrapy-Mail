from django.db import models
from users.models import CustomUser
# Create your models here.


class ScrapingProcess(models.Model):
    custom_user = models.ForeignKey(CustomUser)
    website_lists = ""
    file_result = ""
    #file_source = "" #file_source not needed, will be converted into website_lists string 
    