from django.views.generic import ListView, DetailView, TemplateView

from articles.models import Article


class ArticleListView(ListView):
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()


class UpdateIndexView(TemplateView):
    template_name = "articles/update_index.html"

    def get_context_data(self, **kwargs):
        updated = 0
        for article in Article.objects.all():
            article.update_index()
            article.save()
            updated += 1

        return {
            "count": updated
        }
