from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import empty

from articles.models import Article, ArticleTag


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = ("id", "title",)


class ColorField(serializers.CharField):
    def run_validation(self, data=empty):
        data = super().run_validation(data)
        if data[0] != "#" or len(data) != 7:
            raise ValidationError("Ten kolor jest niepoprawny")
        return data

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return data.lower()


class ArticleSerializer(serializers.ModelSerializer):
    color = ColorField()

    class Meta:
        model = Article
        fields = ("id", "title", "author", "tags", "user", "color")
        extra_kwargs = {
            "tags": {
                "required": False,
                "allow_empty": True
            }
        }
