from django.contrib import admin
from django.utils.html import format_html
from nested_admin.nested import NestedModelAdmin, NestedStackedInline

from bucsani_school.models import PostType, Post, PostImage, PostFile, GalleryImage, Document, SiteConfig


class PostFileAdmin(NestedStackedInline):
    model = PostFile
    extra = 0


class PostImageAdmin(NestedStackedInline):
    model = PostImage
    extra = 0


@admin.register(Post)
class PostAdmin(NestedModelAdmin):
    extra = 0
    # list_display = ('__str__', 'action')
    inlines = [PostImageAdmin, PostFileAdmin]
    filter_horizontal = ["type"]

    # def action(self, obj):
    #     return format_html('<a class="btn" href="/admin/my_app/my_model/{}/delete/">Delete</a>', obj.id)


admin.site.register([PostType, GalleryImage, Document, SiteConfig])
