from django.db import models


class Product(models.Model):
    title = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return f"Produkt {self.title} ${self.price}"

    class Meta:
        abstract = True


class Ebook(Product):
    url_toc = models.URLField()

    def __str__(self):
        return f"Ebook {self.title} ${self.price}"


class Book(Product):
    isbn = models.TextField()

    def __str__(self):
        return f"Książka {self.title} ${self.price}"
