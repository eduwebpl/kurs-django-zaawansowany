from django.contrib.postgres.search import TrigramSimilarity
from django.views.generic import ListView, DetailView

from articles.models import Article


class ArticleListView(ListView):
    queryset = Article.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.filter_queryset(queryset)

    def filter_queryset(self, queryset):
        query = self.request.GET.get('q')
        if query:
            similarity = TrigramSimilarity('title', query)
            queryset = queryset.annotate(similarity=similarity)
        return queryset


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()
