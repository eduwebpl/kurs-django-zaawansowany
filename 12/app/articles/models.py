from django.db import models


class ArticleTag(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title


class Author(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField("ArticleTag")

    def __str__(self):
        return self.title
