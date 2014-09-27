from django.db import models

# Create your models here.

class Venue(models.Model):
	lat = models.IntegerField(default=0)
	lon = models.IntegerField(default=0)
	space = models.IntegerField(default=0)

class Event(models.Model):

class UserCreate(models.Model):
	f_name =  models.CharField(max_length=30)
	l_name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	passwd = models.CharField(max_length=30)

class UserBuy(models.Model):
	f_name =  models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	passwd = models.CharField(max_length=30)

class 