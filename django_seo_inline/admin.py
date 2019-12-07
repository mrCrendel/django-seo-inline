from django.contrib import admin
from nested_admin.nested import NestedGenericStackedInline

from .mixins import Seo


class SeoInline(NestedGenericStackedInline):
    model = Seo
    max_num = 1
    extra = 1


class SeoAdminMixin:
    def get_inline_instances(self, request, obj=None):
        if SeoInline not in self.inlines:
            self.inlines += (SeoInline,)
        return super().get_inline_instances(request, obj)


@admin.register(Seo)
class SeoAdmin(admin.ModelAdmin):
    exclude = ('object_id',)
