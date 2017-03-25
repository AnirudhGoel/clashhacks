from django.db import models

# Create your models here.
class Skill(models.Model):
	skillID = models.IntegerField(max_length=10, primary_key=True)
	skillName = models.CharField(max_length=40, default="")

class Login(models.Model):
	userId = models.IntegerField(max_length=10, primary_key=True)
	username = models.CharField(max_length=40, default="")
	password = models.CharField(max_length=40, default="")

class User(models.Model):
	userId = models.IntegerField(max_length=10, primary_key=True)
	Name = models.CharField(max_length=40)

class Rating(models.Model):
	userId = models.IntegerField(max_length=10)
	skillID = models.IntegerField(max_length=10)
	rating = models.IntegerField(max_length=1)

class Transaction(models.Model):
	teach = models.IntegerField(max_length=10)
	learn = models.IntegerField(max_length=10)
	byTime = models.BooleanField()
	value = models.IntegerField(max_length=10)