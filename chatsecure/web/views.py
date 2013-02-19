from django.shortcuts import render_to_response
from django.template import RequestContext


def nav_items():
    nav_items = []
    nav_items.append(dict({'title': 'About', 'slug': 'about'}))
    nav_items.append(dict({'title': 'Blog', 'slug': 'blog'}))
    nav_items.append(dict({'title': 'Contribute', 'slug': 'contribute'}))
    nav_items.append(dict({'title': 'Contact', 'slug': 'contact'}))
    return nav_items


def about(request):
    return render_to_response('about.html', {
            'nav_items': nav_items(),
            'slug': 'about',
        }, RequestContext(request))


def contribute(request):
    return render_to_response('contribute.html', {
            'nav_items': nav_items(),
            'slug': 'contribute',
        }, RequestContext(request))


def contact(request):
    return render_to_response('contact.html', {
            'nav_items': nav_items(),
            'slug': 'contact',
        }, RequestContext(request))

def root(request):
    return render_to_response('about.html', {
            'nav_items': nav_items(),
            'slug': 'about',
        }, RequestContext(request))

def webmaster_verification(request):
    return render_to_response('google319cdfb15ceafd92.html')
