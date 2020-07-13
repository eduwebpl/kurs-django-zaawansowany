from django.db import models


class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Artykuł"
        verbose_name_plural = "Artykuły"

    def __str__(self):
        return self.title

    def publish(self):
        self.is_published = True
        self.save()

    def unpublish(self):
        self.is_published = False
        self.save()
