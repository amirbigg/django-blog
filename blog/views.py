from django.shortcuts import render
from .models import Article


def all_articles(request):
	all_articles = Article.objects.all()
	return render(request, 'blog/all_articles.html', {'all_articles':all_articles})


def article_detail(request, id, slug):
	article = Article.objects.get(id=id, slug=slug)
	return render(request, 'blog/article.html', {'article':article})