from django.shortcuts import render_to_response
from core.models import Post
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse

class PostCreate(CreateView):
	model = Post
	def get_success_url(self):
		return reverse('home')