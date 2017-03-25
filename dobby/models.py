from django.db import models

# Create your models here.
class Skill(models.Model):
	skillID = models.IntegerField(primary_key=True)
	skillName = models.CharField(max_length=40, default="")

class Login(models.Model):
	userId = models.IntegerField(primary_key=True)
	username = models.CharField(max_length=40, default="")
	password = models.CharField(max_length=40, default="")

class User(models.Model):
	userId = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=40, default="")
	status = models.CharField(max_length=80, default="")
	location = models.CharField(max_length=40, default="")
	mobile = models.BigIntegerField()

class Rating(models.Model):
	userId = models.IntegerField()
	skillID = models.IntegerField()
	rating = models.IntegerField()

class CompletedTransaction(models.Model):
	teach = models.IntegerField()
	learn = models.IntegerField()
	topic = models.CharField(max_length=30)
	byTime = models.BooleanField()
	value = models.IntegerField()

class PendingTransaction(models.Model):
	teacherId = models.IntegerField()
	learnerId = models.IntegerField()
	skillId = models.IntegerField()