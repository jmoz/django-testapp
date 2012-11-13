from django.conf.urls.defaults import *
from core.views import PostCreate

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url(r'^post/add/$', PostCreate.as_view(), name='post_add'),
    url('^$', 'core.views.home', name='home'),
)
