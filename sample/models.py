from django.db import models
from django_seo_inline.mixins import SeoModelMixin
from solo.models import SingletonModel


class SampleSoloModel(SeoModelMixin, SingletonModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='solo/', blank=True, null=True)

    def __str__(self):
        return self.title


class SampleModel(SeoModelMixin, models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='standart/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/samples/{self.pk}"
