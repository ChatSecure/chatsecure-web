from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chatsecure.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Move to web.urls if possible
    # url(r'^$', include('web.urls')),
    url(r'^about/', 'web.views.about'),
    url(r'^contribute/', 'web.views.contribute'),
    url(r'^contact/', 'web.views.contact'),
    url(r'^google319cdfb15ceafd92.html', 'web.views.webmaster_verification'),

    url(r'^$', 'web.views.root'),
)
