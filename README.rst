=================
Django Seo Inline
=================

Django Seo Inline is a simple application that provides the basic seo meta attributes as title, description and
keywords. for use in Django models from Django version 1.11+.

INSTALLATION
------------
- ``pip install git@github.com:mrCrendel/django-seo-inline.git``
- ``pip install django-seo-inline``


QUICK START
-----------

1. Add "django_seo_inline" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_seo_inline',
        ...
    ]

2. Create a model for which you want to use seo::

    from django.db import models
    from django_seo_inline.mixins import SeoModelMixin

    class SampleModel(SeoModelMixin, models.Model):
        pass

3. in the ``admin.py`` include the following::

    from django_seo_inline.admin import SeoAdminMixin

    @admin.register(SampleModel)
    class SampleModel(SeoAdminMixin, admin.ModelAdmin):
        pass

4. In ``views`` we add ``SeoListMixin`` for generic ``ListView``, ``SeoDetailMixin`` for ``generic DetailView``::


    class SampleListView(SeoListMixin, ListView):
        model = SampleModel
        ...

    class SampleDetailView(SeoDetailMixin, DetailView):
        model = SampleModel
        ...

5. Also packages supports generic ``TemplateView`` and others by ``PageMixinView`` just don't forget show ``seo_model`` field::

    class IndexView(PageMixinView, TemplateView):
        ...
        seo_model = SampleSoloModel
        ...

6
- Run ``python manage.py makemigrations`` to create migrations for seo relations.
- Run ``python manage.py migrate``

7. in template ``base.html`` include ``{% include "seo/seo.html" %}`` in you header block.