from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(?P<post_slug>[a-zA-Z0-9_.-]+)', 'blog.views.view_post'),

    url(r'^$', 'blog.views.root'),
)
