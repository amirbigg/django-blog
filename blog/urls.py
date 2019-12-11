from django.urls import path
from . import views


urlpatterns = [
	path('all_articles/', views.all_articles, name='all_articles'),
]