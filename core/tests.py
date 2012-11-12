"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from core.models import Post


class PostTest(TestCase):
	def testPostObject(self):
		p = Post()
		p.title = 'foo'
		p.text = 'footext'

		self.assertEqual('foo', p.title)
		self.assertEqual('footext', p.text)
