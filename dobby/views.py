from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import json

# from .models import Calender



def index(request):
	context = ""
	return render(request, 'dobby/index.html', context)