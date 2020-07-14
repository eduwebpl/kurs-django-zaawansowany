import time

from django.db import models


class Author(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

    @property
    def total_articles_count(self):
        time.sleep(1)
        return self.article_set.count()


class ArticleTag(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(ArticleTag)

    def __str__(self):
        return self.title
