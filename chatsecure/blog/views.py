from web.views import nav_items
from django.views import generic
from blog.models import Post
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


class BlogIndexView(generic.ArchiveIndexView):
    template_name = 'blog.html'
    model = Post
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        ctx = super(BlogIndexView, self).get_context_data(**kwargs)
        ctx['nav_items'] = nav_items()  # add something to ctx
        ctx['slug'] = 'blog'
        return ctx


def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render_to_response('blog_post.html', {
            'nav_items': nav_items(),
            'slug': 'blog',
            'post': post,
        }, RequestContext(request))


def root(request):
    return ''
