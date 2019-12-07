from django.contrib.contenttypes.models import ContentType

from django_seo_inline.mixins import Seo


class SeoListMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        content_type = ContentType.objects.get_for_model(self.model)
        context['seo'] = Seo.objects.filter(object_id=None, content_type=content_type).first()
        return context


class SeoDetailMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['seo'] = self.object.seo_for_detail
        return context


class PageMixinView:

    def dispatch(self, request, *args, **kwargs):
        if not self.seo_model:
            raise AttributeError
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        content_type = ContentType.objects.get_for_model(self.seo_model)
        context['seo'] = Seo.objects.filter(object_id=None, content_type=content_type).first()
        return context
