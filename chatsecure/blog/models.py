from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    body = models.TextField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%s/" % self.slug
