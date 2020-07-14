from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers, vary_on_cookie
from django.views.generic import ListView, DetailView

from articles.models import Article


class ArticleListView(ListView):
    queryset = Article.objects.all()

    @method_decorator(cache_page(60))
    @method_decorator(vary_on_headers('User-Agent'))
    @method_decorator(vary_on_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()
