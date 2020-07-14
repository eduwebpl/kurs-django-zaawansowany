from django.contrib.postgres.search import TrigramSimilarity, SearchRank, SearchVector, SearchQuery
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
            search_vector = SearchVector('title', weight="A") + SearchVector('content', weight='B')
            search_query = SearchQuery(query)
            rank = SearchRank(search_vector, search_query)
            queryset = queryset.annotate(rank=rank).order_by('-rank').filter(rank__gt=0)
        return queryset


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()
