from django.db import models
from datetime import datetime
# Create your models here.

class List(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=10000)
	create_at = models.DateTimeField(default=datetime.now, blank=True)