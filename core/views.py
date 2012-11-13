from django.shortcuts import render_to_response
from core.models import Post

def home(request):
	posts = Post.objects.all().order_by('-date_created')[:10]
	return render_to_response('core/index.html', {'posts': posts})