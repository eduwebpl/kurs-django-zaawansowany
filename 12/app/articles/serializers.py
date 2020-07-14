from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from articles.models import Article, ArticleTag


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = ("id", "title",)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "author", "tags")
        extra_kwargs = {
            "tags": {
                "required": False,
                "allow_empty": True
            },
            "author": {
                "required": True,
                "allow_null": False
            }
        }

    def validate_title(self, value):
        prohibited_words = ["łobuz", "gałgan"]
        words = value.lower().split(" ")
        for prohibited_word in prohibited_words:
            if prohibited_word in words:
                raise ValidationError("Tytuł nie może zawierać brzydkich słów")
        return value

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if attrs.get('title') == attrs.get('author').title:
            raise ValidationError({
                "title": "Tytuł nie może być taki jak nazwa autora"
            })
        return attrs
