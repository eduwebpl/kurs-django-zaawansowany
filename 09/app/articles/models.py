from django.db import models


class Author(models.Model):
    name = models.TextField()


class ArticleTag(models.Model):
    name = models.TextField()


class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(ArticleTag)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def publish(self):
        self.is_published = True
        self.save()

    def unpublish(self):
        self.is_published = False
        self.save()
