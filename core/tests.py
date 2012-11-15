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

	def testAddingTags(self):
		p = Post()
		p.title = 'foo'
		p.text = 'footext'
		p.tags = ['foo', 'bar']
		p.save()

		self.assertEqual(2, len(p.tags))

		p = Post()
		p.title = 'foo2'
		p.text = 'footext2'
		p.tags = ['foo']
		p.save()
		
		result = Post.objects.filter(tags='foo')
		self.assertEqual(2, len(result))

		result = Post.objects.filter(tags='bar')
		self.assertEqual(1, len(result))

		result = Post.objects.filter(tags='baz')
		self.assertEqual(0, len(result))