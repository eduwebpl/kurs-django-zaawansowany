from articles.models import ArticleTag, Author, Article
from articles.serializers import ArticleSerializer


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
