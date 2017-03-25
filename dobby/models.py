from django.db import models

# Create your models here.
class Skills(models.Model):
	event_id = models.CharField(max_length=40, primary_key=True)
	event_google_id = models.CharField(max_length=40, default="")