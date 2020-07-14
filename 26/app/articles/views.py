from django.db.models import Q
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
            words = query.split(" ")
            q_object = Q()
            for word in words:
                q_object.add(Q(title__icontains=word), Q.OR)
            queryset = queryset.filter(q_object)
        return queryset


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()
