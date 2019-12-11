from django.urls import path
from . import views


urlpatterns = [
	path('', views.all_articles, name='all_articles'),
]