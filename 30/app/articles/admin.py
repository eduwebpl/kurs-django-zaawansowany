from django.contrib import admin

from articles.models import Article, Author


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "rating", "author")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
