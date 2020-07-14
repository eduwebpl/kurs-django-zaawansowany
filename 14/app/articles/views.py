from django.views.generic import ListView, DetailView
from rest_framework.generics import ListCreateAPIView

from articles.models import Article
from articles.serializers import ArticleSerializer


class ArticleListView(ListView):
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()


class ArticleListCreateView(ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
