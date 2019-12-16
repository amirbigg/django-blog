from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'writer', 'publish', 'status')
	list_filter = ('status', 'writer', 'publish')
	list_editable = ('status',)
	search_fields = ('title', 'body')
	raw_id_fields = ('writer',)
	prepopulated_fields = {'slug':('title',)}
