from django.conf.urls import patterns, url
from blog.models import Post
from blog.views import BlogIndexView, BlogPostView

urlpatterns = patterns('',
 #   (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[0-9A-Za-z-]+)/$', 'object_detail', dict(blog_dict, slug_field='slug')),
 #   (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',  'archive_day', blog_dict),
 #   (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',  'archive_month', blog_dict),
 #   (r'^(?P<year>\d{4})/$',  'archive_year',  blog_dict),
  #  (r'^/?$',  'archive_index', blog_dict), )
    url(r'^$', BlogIndexView.as_view(
        model=Post, paginate_by=5,
        date_field='date')),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>\d+)/$',
        BlogPostView.as_view(model=Post, date_field="date")),
)
