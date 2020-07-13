import pytest

from articles.models import Article


@pytest.fixture
def article():
    return Article.objects.create(
        title="Tytuł artykułu"
    )


def test_publish_article(article):
    article.publish()
    article.refresh_from_db()
    assert article.is_published


def test_unpublish_article(article):
    article.unpublish()
    article.refresh_from_db()
    assert not article.is_published
