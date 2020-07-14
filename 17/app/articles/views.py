from django.db.models import Prefetch
from django.views.generic import ListView, DetailView

from articles.models import Article, ArticleTag


class ArticleListView(ListView):
    queryset = Article.objects.all().prefetch_related("author", "tags")


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()
