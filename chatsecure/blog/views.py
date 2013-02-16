from django.shortcuts import render_to_response
from django.template import RequestContext
from web.views import nav_items


def root(request):
    return render_to_response('blog.html', {
            'nav_items': nav_items(),
            'slug': 'blog',
        }, RequestContext(request))
