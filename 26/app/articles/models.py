from django.db import models


class Article(models.Model):
    title = models.TextField()
    content = models.TextField()

    class Meta:
        verbose_name = "Artykuł"
        verbose_name_plural = "Artykuły"

    def __str__(self):
        return self.title
