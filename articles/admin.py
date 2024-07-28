from django.contrib import admin

# Register your models here.

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'timestamp', 'updated', 'publish']
    search_fields = ['title', 'content']

admin.site.register(Article, ArticleAdmin)

"""
admin: abodo
pwd: Ngoabel1
"""