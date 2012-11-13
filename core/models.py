from django.db import models
from django.forms import ModelForm
from datetime import datetime

class Post(models.Model):
	title = models.CharField(max_length=200)
	text = models.CharField(max_length=255)
	date_created = models.DateTimeField(auto_now_add=True)

	@property
	def time_ago(self):
		td = datetime.now() - self.date_created
		if td.days >= 7:
			weeks = td.days / 7
			return "%s week%s ago" % (weeks, '' if weeks == 1 else 's')
		elif td.days > 0:
			return "%s day%s ago" % (td.days, '' if td.days == 1 else 's')
		elif td.seconds >= 3600:
			hours = td.seconds / 3600
			return "%s hour%s ago" % (hours, '' if hours == 1 else 's')
		elif 60 <= td.seconds < 3600 :
			mins = td.seconds / 60
			return "%s minute%s ago" % (mins, '' if mins == 1 else 's')
		else:
			return 'Just now'


class PostForm(ModelForm):
	class Meta:
		model = Post