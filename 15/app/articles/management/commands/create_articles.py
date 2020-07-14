from django.core.management.base import BaseCommand
from faker import Faker
from model_bakery.recipe import Recipe, related

from articles.models import Article, ArticleTag

fake = Faker("pl_PL")

article_tag = Recipe(
    ArticleTag,
    name=lambda: fake.word()
)

article = Recipe(
    Article,
    title=lambda: f"Artykuł o zawodzie - {fake.job()}",
    author__name=lambda: fake.name(),
    content=lambda: fake.text(max_nb_chars=500),
    tags=related(article_tag),
)


class Command(BaseCommand):
    help = 'Creates sample articles'

    def add_arguments(self, parser):
        parser.add_argument('how_many', type=int)

    def handle(self, *args, **options):
        articles = [
            self.get_article() for _ in range(options["how_many"])
        ]
        count = len(articles)
        self.stdout.write(self.style.SUCCESS(f'Created {count} articles'))

    @staticmethod
    def get_article():
        return article.make()
