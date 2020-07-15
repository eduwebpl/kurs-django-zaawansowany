from django.db import models
from django.db.models import F

from core.mixins import CreateModifiedMixin


class ArticleTag(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Article(CreateModifiedMixin):
    title = models.TextField()
    content = models.TextField()
    rating = models.PositiveIntegerField(
        choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6),)
    )
    tags = models.ManyToManyField("ArticleTag")
    author = models.ForeignKey(
        "Author",
        related_name="articles",
        on_delete=models.CASCADE
    )
    views = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    def increment_views(self):
        self.views = F('views') + 1
        self.save()
