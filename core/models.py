from django.db import models
from django.forms import ModelForm

class Post(models.Model):
	title = models.CharField(max_length=200)
	text = models.CharField(max_length=255)
	date_created = models.DateTimeField(auto_now_add=True)

class PostForm(ModelForm):
	class Meta:
		model = Post