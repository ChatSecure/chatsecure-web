from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
