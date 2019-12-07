from django.contrib import admin

from django_seo_inline.admin import SeoAdminMixin
from .models import SampleModel, SampleSoloModel
from solo.admin import SingletonModelAdmin


@admin.register(SampleSoloModel)
class SampleSoloModelAdmin(SingletonModelAdmin):
    pass


@admin.register(SampleModel)
class SampleModel(SeoAdminMixin, admin.ModelAdmin):
    pass
