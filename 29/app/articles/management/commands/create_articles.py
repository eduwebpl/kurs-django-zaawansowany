from random import randint

from django.core.management.base import BaseCommand
from django.utils.lorem_ipsum import sentence, words

from articles.models import Article


class Command(BaseCommand):
    help = 'Creates sample articles'

    def add_arguments(self, parser):
        parser.add_argument('how_many', type=int)

    def handle(self, *args, **options):
        articles = [
            self.get_article() for _ in range(options["how_many"])
        ]
        count = len(Article.objects.bulk_create(articles))
        self.stdout.write(self.style.SUCCESS(f'Created {count} articles'))

    @staticmethod
    def get_article():
        return Article(
            title=words(randint(3, 12), common=False).capitalize(),
            content=sentence()
        )
