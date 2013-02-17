from django.conf.urls import patterns, url
from blog.models import Post
from blog.views import BlogIndexView

urlpatterns = patterns('',
    url(r'^$', BlogIndexView.as_view(
        model=Post,
        paginate_by=5,
        date_field='date')),
    url(r'^(?P<slug>[a-zA-Z0-9-]+)', 'blog.views.view_post'),
)
