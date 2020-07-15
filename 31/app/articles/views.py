from django.db.models import F
from django.views.generic import ListView, DetailView
from rest_framework.response import Response
from rest_framework.views import APIView

from articles.models import Article


class ArticleListView(ListView):
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()


class ArticleListAPIView(APIView):
    def get(self, request, **kwargs):
        articles = Article.objects.annotate(x=F('title')).values_list('id', 'x')
        return Response(articles)
