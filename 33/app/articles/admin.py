from django.contrib import admin

from articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ("index_field",)
