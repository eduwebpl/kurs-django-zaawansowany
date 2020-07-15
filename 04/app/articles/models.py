from django.db import models

from core.mixins import CreateModifiedMixin


class Article(CreateModifiedMixin):
    title = models.TextField()
    content = models.TextField()

    class Meta:
        verbose_name = "Artykuł"
        verbose_name_plural = "Artykuły"

    def __str__(self):
        return self.title
