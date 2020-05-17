from django.db import models
from django.utils.text import slugify
# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=300,blank=True,null=True)
    description  = models.TextField(max_length=2000,blank=True,null=True)
    deadline = models.DateField(blank=True,null=True)
    complete = models.BooleanField(default=False,blank=True,null=True)
    taskOwner = models.CharField(max_length=100,blank=True,null=True,default='')
    taskSlug = models.SlugField(blank=True,null=True,default='')
    
    def __str__(self):
        return self.title
    