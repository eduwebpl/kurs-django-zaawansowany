from django.views.generic import ListView, DetailView, TemplateView

from articles.models import Article


class ArticleListView(ListView):
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()


class UpdateIndexView(TemplateView):
    template_name = "articles/update_index.html"

    def get_context_data(self, **kwargs):
        articles_to_update = Article.objects.all()
        for article in articles_to_update:
            article.update_index()
        Article.objects.bulk_update(articles_to_update, fields=['index_field'])
        return {
            "count": articles_to_update.count()
        }
