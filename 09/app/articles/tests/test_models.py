import pytest
from model_bakery import baker
from model_bakery.recipe import Recipe, related

from articles.models import Article, Author, ArticleTag


@pytest.fixture
def article():
    return baker.make(Article)


def test_publish_article(article):
    article.publish()
    article.refresh_from_db()
    assert article.is_published


def test_unpublish_article(article):
    article.unpublish()
    article.refresh_from_db()
    assert not article.is_published


def test_article_has_author(article):
    assert article.author


def test_author_jan_kowalski():
    article = baker.make(Article, author__name="Jan Kowalski")
    assert article.author.name == "Jan Kowalski"


def test_tags():
    article = baker.make(Article, tags__name="TEST")
    assert article.tags.count() == 5
    assert article.tags.filter(name="TEST").count() == 5


def test_article_with_existing_author():
    author = baker.make(Author, name="Jan Kowalski")
    article = baker.make(Article, author=author)
    assert article.author == author


tag_recipe = Recipe(
    ArticleTag
)
article_recipe = Recipe(
    Article,
    title="tytuł",
    tags=related(tag_recipe)
)


def test_article_from_recipe():
    article = article_recipe.make()
    assert article.title == "tytuł"
