from django import template
from django.template.loader import render_to_string
register = template.Library()


@register.simple_tag
def render_post(post):
    return render_to_string('tags/post.html', {'post': post})
