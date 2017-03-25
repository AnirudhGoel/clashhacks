from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import json

from .models import Skill, Login, Rating, User, CompletedTransaction, PendingTransaction



def index(request):
	context = ""
	return render(request, 'dobby/index.html', context)

def home(request, userId):
	q = User.objects.get(userId = userId)
	name = q.name
	status = q.status
	location = q.location

	q = Login.objects.get(userId = userId)
	username = q.username
	context = {
		'userId': userId,
		'name': name,
		'username': username,
		'status': status,
		'location': location,
	}
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
			return HttpResponse(json.dumps({"response": "valid", "userId": q.userId}), content_type = "application/json")
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

def compTransaction(request):
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

def pendTransaction(request):
	pass



def pendingTeacher(request):
	userId = request.GET['userId']
	response = {}

	if PendingTransaction.objects.filter(teacherId = userId).count() != 0:
		q = PendingTransaction.objects.filter(teacherId = userId).values()
		for x in range(0,q.count()):
			learnerId = q[x]["learnerId"]
			skillId = q[x]["skillId"]

			p = User.objects.get(userId = learnerId)
			r = Skill.objects.get(skillId = skillId)

			response[x] = {}
			response[x]["learnerName"] = p.name
			response[x]["location"] = p.location
			response[x]["mobile"] = p.mobile
			response[x]["skillName"] = r.skillName
		return HttpResponse(json.dumps({"response": response}), content_type = "application/json")
	else:
		return HttpResponse(json.dumps({"response": "None"}), content_type = "application/json")


def search(request):
	context = ""
	return render(request, 'dobby/search.html', context)