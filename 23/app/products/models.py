from django.db import models


class Product(models.Model):
    title = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return f"Produkt {self.title} ${self.price}"
