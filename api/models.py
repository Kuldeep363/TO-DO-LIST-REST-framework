from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=300,blank=True,null=True)
    description  = models.TextField(max_length=2000,blank=True,null=True)
    deadline = models.DateField(blank=True,null=True)
    complete = models.BooleanField(default=False,blank=True,null=True)
    taskSlug = models.SlugField(blank=True,null=True,default='')
    taskOwner = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.title
    