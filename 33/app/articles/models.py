from django.db import models
from unidecode import unidecode


class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    index_field = models.TextField(blank=True)

    class Meta:
        verbose_name = "Artykuł"
        verbose_name_plural = "Artykuły"

    def __str__(self):
        return self.title

    def update_index(self):
        self.index_field = f"{unidecode(self.title)} {unidecode(self.content)}"
