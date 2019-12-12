from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
	path('', views.all_articles, name='all_articles'),
	path('<int:id>/<slug:slug>/', views.article_detail, name='article_detail'),
]