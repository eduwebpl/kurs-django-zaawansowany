from rest_framework import serializers

from articles.models import Article, ArticleTag


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = ("id", "title",)


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    tags = ArticleTagSerializer(many=True)

    class Meta:
        model = Article
        fields = ("id", "title", "author", "tags")
