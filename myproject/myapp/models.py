from django.db import models

# Create your models here.
class Author(models.Model):
  # name = models.CharField(max_length=100,null=True,blank=True)
  age =models.IntegerField(null=True)
  age1 =models.IntegerField(null=True)
  # pass


class Blog(models.Model):
  title = models.CharField(max_length=100,null=True,blank=True)
  age2 =models.IntegerField(null=True)
  # age1 =models.IntegerField(null=True)
