from articles.models import Author, Article


def test_total_articles_count():
    author = Author.objects.create()
    Article.objects.create(author=author)
    Article.objects.create(author=author)
    assert author.total_articles_count == 2
    Article.objects.create(author=author)
    author = Author.objects.get()
    assert author.total_articles_count == 3
