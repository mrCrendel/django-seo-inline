from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models


class Seo(models.Model):
    class Meta:
        # unique_together = ['object_id', 'content_type']
        constraints = [
            models.UniqueConstraint(fields=['object_id', 'content_type'], name='unique_content_type'),
        ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey()

    def validate_unique(self, *args, **kwargs):
        super(Seo, self).validate_unique(*args, **kwargs)
        try:
            action = False
            if self.content_type:
                action = True
        except:
            action = False

        if action:
            if self.__class__.objects. \
                    filter(content_type=self.content_type, object_id=self.object_id). \
                    exists():
                raise ValidationError(
                    message='Seo with this (content_type, object_id) already exists.',
                    code='unique_together',
                )


class SeoModelMixin:
    seo = GenericRelation(Seo)

    @property
    def seo_for_detail(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        try:
            return Seo.objects.get(object_id=self.id, content_type=content_type)
        except Seo.DoesNotExist:
            return None
        except Seo.MultipleObjectsReturned:
            return Seo.objects.filter(object_id=self.id, content_type=content_type).first()