from django.contrib import admin
from .models import Article, Author, Gallery, Comment
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'is_published',
                    'pub_date','author')
    list_display_links = ('id','title')
    list_filter = ('author',)
    list_editable = ('is_published',)
    search_fields = ('title','description','category')
    list_per_page = 10


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user','is_member','hire_date')
    list_display_links = ('user',)
    list_per_page = 10
    search_fields = ('user',)
    list_editable = ('is_member',)

admin.site.register(Author,AuthorAdmin)    
admin.site.register(Article,ArticleAdmin)
admin.site.register(Gallery)
admin.site.register(Comment)