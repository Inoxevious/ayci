from django.contrib import admin
from account.models import AccountUser
from .models import Article, Author, Gallery, Comment
from django.contrib.auth.models import User
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_staff:
            return qs
        return qs.filter(author=request.user)


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