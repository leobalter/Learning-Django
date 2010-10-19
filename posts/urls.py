from django.conf.urls.defaults import *

urlpatterns = patterns('posts.views',
    (r'^$', 'index'),
    (r'^(?P<post_id>\d+)/$', 'detail'),
)