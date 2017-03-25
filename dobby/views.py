from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import json

from .models import Skill, Login, Rating, User, Transaction



def index(request):
	context = ""
	return render(request, 'dobby/index.html', context)

def home(request):
	context = ""
	return render(request, 'dobby/home.html', context)

def profile(request):
	context = ""
	return render(request, 'dobby/profile.html', context)

def login(request):
	username = request.GET['username']
	password = request.GET['password']

	try:
		q = Login.objects.get(username = username)
		if q.password == password:
			return HttpResponse(json.dumps({"response": "valid"}), content_type = "application/json")
		else:
			return HttpResponse(json.dumps({"response": "invalid", "message": "Invalid Password"}), content_type = "application/json")
	except Login.DoesNotExist:
		return HttpResponse(json.dumps({"response": "invalid", "message": "User does not exist"}), content_type = "application/json")

def rating(request):
	userId = request.GET['userId']
	skillId = request.GET['skillId']
	rating = request.GET['rating']

	q = Rating(userId = userId, skillId = skillId, rating = rating)
	try:
		q.save()
		result = "success"
	except Exception as e:
		result = "unsuccess: " + e

	return HttpResponse(json.dumps({"response": result, "message": "Error saving data"}), content_type = "application/json")

def transaction(request):
	teach = request.GET['teach']
	learn = request.GET['learn']
	byTime = request.GET['byTime']
	value = request.GET['value']

	q = Rating(teach = teach, learn = learn, byTime = byTime, value = value)
	try:
		q.save()
		result = "success"
	except Exception as e:
		result = "unsuccess: " + e

	return HttpResponse(json.dumps({"response": result, "message": "Error saving data"}), content_type = "application/json")