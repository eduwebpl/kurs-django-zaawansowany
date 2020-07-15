from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView

from articles.models import Article


class ArticleListView(ListView):
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()


class ArticleListAPIView(View):
    def get(self, request, **kwargs):
        return JsonResponse({})
