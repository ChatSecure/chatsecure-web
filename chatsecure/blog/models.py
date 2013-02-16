from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Post(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    body = models.TextField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    # http://www.rossp.org/blog/2006/jan/23/building-blog-django-1/
    def get_absolute_url(self):
        return "/blog/%s/%s/" % (self.date.strftime("%Y/%m/%d").lower(), self.slug)
