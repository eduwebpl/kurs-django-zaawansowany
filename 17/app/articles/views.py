from django.views.generic import ListView, DetailView

from articles.models import Article


class ArticleListView(ListView):
    queryset = Article.objects.all().select_related("author")


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()
