from django.db import models


class ArticleTag(models.Model):
    title = models.TextField()


class Author(models.Model):
    title = models.TextField()


class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField("ArticleTag")

    class Meta:
        verbose_name = "Artykuł"
        verbose_name_plural = "Artykuły"

    def __str__(self):
        return self.title
