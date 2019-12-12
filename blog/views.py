from django.shortcuts import render, get_object_or_404
from .models import Article


def all_articles(request):
	all_articles = Article.published.all()
	return render(request, 'blog/all_articles.html', {'all_articles':all_articles})


def article_detail(request, id, slug):
	article = get_object_or_404(Article, id=id, slug=slug)
	return render(request, 'blog/article.html', {'article':article})