import pytest
from rest_framework.exceptions import ValidationError

from articles.models import ArticleTag, Author, Article
from articles.serializers import ArticleSerializer, ColorField


def test_article_create_by_serializer():
    tag = ArticleTag.objects.create(title="test")

    data = {
        "title": "test",
        "tags": [tag.id]
    }
    serializer = ArticleSerializer(data=data)
    assert serializer.is_valid()
    article = serializer.save()


def test_article_representation():
    tag = ArticleTag.objects.create(title="test")
    author = Author.objects.create(title="test")
    article = Article.objects.create(
        title="x",
        author=author
    )
    article.tags.add(tag)

    serializer = ArticleSerializer(article)

    print()


def test_color_field_validation():
    color_field = ColorField()
    with pytest.raises(ValidationError):
        color_field.run_validation("abc")
    color_field.run_validation("#ffffff")


def test_uppercase_color():
    color_field = ColorField()
    data = color_field.to_internal_value("#ffffff")
    assert data == "#FFFFFF"
