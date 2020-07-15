from django.db import models

from core.mixins import CreateModifiedMixin


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
    author = models.ForeignKey(
        "Author",
        related_name="articles",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
