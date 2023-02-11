from django.db import models

# Create your models here.

class Rank(models.Model):
    rank = models.CharField(null=False,blank=False,max_length=20)

class Csd_id(models.Model):
    serial = models.AutoField(primary_key=True)
    name = models.CharField(null=False,blank=False,max_length=30)
    photo = models.ImageField(null=False,blank=False,upload_to='images')
    rank = models.OneToOneField(Rank,on_delete=models.DO_NOTHING)

