from django.shortcuts import render_to_response
from core.models import Post
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse

class PostCreate(CreateView):
	model = Post
	def get_success_url(self):
		return reverse('home')


class TaggedList(ListView):
	context_object_name = 'posts'
	template_name = 'core/index.html'
	def get_queryset(self):
		tags = self.kwargs['tag']
		return Post.objects.filter(tags=tags).order_by('-date_created')[:10]