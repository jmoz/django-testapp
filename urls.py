from django.conf.urls.defaults import *
from core.views import PostCreate
from core.models import Post
from django.views.generic import ListView

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url(r'^post/add/$', PostCreate.as_view(), name='post_add'),
    url('^$', 
    	ListView.as_view(
    		queryset=Post.objects.all().order_by('-date_created')[:10],
    		context_object_name='posts',
    		template_name='core/index.html'), 
    	name='home'),
)
