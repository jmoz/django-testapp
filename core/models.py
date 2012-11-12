from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)