from django.db import models

# Create your models here.
class user(models.Model):
    email = models.EmailField()
    codechef = models.IntegerField(default=0)
    codeforces = models.IntegerField(default=0)
    hackerearth = models.IntegerField(default=0)
    hackerrank = models.IntegerField(default=0)
    spoj = models.IntegerField(default=0)
    password = models.CharField(max_length=30)
    no = models.CharField(max_length=10,default='u')