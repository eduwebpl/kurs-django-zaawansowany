from rest_framework import serializers

from articles.models import Article, ArticleTag


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = ("id", "title",)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "author", "tags", "user")
        extra_kwargs = {
            "tags": {
                "required": False,
                "allow_empty": True
            }
        }

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        request = self.context.get('request')
        if request and request.user.pk:
            data['user'] = request.user
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            k.upper(): v for k, v in data.items()
        }
