from web.views import nav_items
from django.views import generic
from blog.models import Post


class BlogIndexView(generic.ArchiveIndexView):
    template_name = 'blog.html'
    model = Post
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        ctx = super(BlogIndexView, self).get_context_data(**kwargs)
        ctx['nav_items'] = nav_items()  # add something to ctx
        ctx['slug'] = 'blog'
        return ctx


class BlogPostView(generic.DateDetailView):
    template_name = 'blog.html'
    model = Post
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        ctx = super(BlogPostView, self).get_context_data(**kwargs)
        ctx['nav_items'] = nav_items()  # add something to ctx
        ctx['slug'] = 'blog'
        return ctx


def root(request):
    return 'asdf'
