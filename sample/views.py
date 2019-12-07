from django.contrib.contenttypes.models import ContentType
from django.views import generic as generic_views

from django_seo_inline.mixins import Seo
from django_seo_inline.views import SeoListMixin, SeoDetailMixin, PageMixinView
from .models import *


class IndexView(PageMixinView, generic_views.TemplateView):
    template_name = 'index.html'
    seo_model = SampleSoloModel

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class SampleListView(SeoListMixin, generic_views.ListView):
    template_name = 'sample_list.html'
    model = SampleModel


class SampleDetailView(SeoDetailMixin, generic_views.DetailView):
    template_name = 'sample_detail.html'
    model = SampleModel
