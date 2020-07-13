import pytest

from articles.models import Article


@pytest.fixture
def article():
    return Article.objects.create(
        title="Tytuł artykułu"
    )


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass
