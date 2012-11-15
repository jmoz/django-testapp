from django.db import models
from django.forms import ModelForm, CharField
from datetime import datetime
from djangotoolbox.fields import ListField


class StringListField(CharField):
	def prepare_value(self, value):
		return ', '.join(value)

	def to_python(self, value):
		if not value:
			return []
		return [item.strip() for item in value.split(',')]


class TagsField(ListField):
	"""extend and implement formfield to fix error"""
	def formfield(self, **kwargs):
		return models.Field.formfield(self, StringListField, **kwargs)


class Post(models.Model):
	title = models.CharField(max_length=200)
	text = models.CharField(max_length=255)
	date_created = models.DateTimeField(auto_now_add=True)
	tags = TagsField()

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