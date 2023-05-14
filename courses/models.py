from django.db import models

# Create your models here.
class courses(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    