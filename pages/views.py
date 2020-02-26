from django.shortcuts import render
from django.http import HttpResponse
# from listings.choices import price_choices, bedroom_choices, state_choices
from articles.models import Article, Author, Comment ,Gallery
from django.shortcuts import render ,get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from . models import MenuItem, Menu, SubItem, SubMenu

def index(request):
    article = Article.objects.order_by('-pub_date').filter(is_published = True)[:3]
    banner = Gallery.objects.order_by('-pub_date').filter(is_published = True).filter(category='banner')[:3]
    magazines = Gallery.objects.order_by('-pub_date').filter(is_published = True).filter(category='events')[:3]
    videos = Gallery.objects.order_by('-pub_date').filter(is_published = True).filter(category='video')
    events = Gallery.objects.order_by('-pub_date').filter(is_published = True).filter(category='events')[:1]
    products = Gallery.objects.order_by('-pub_date').filter(is_published = True).filter(category='products')[:1]
    ads = Gallery.objects.order_by('-pub_date').filter(is_published = True).filter(category='ads')[:1]
    paginator = Paginator(videos,3)
    page = request.GET.get('page')
    paged_videos = paginator.get_page(page)
    menu = Menu.objects.all()



        
  

    context =  {
        'article':article,
        'banner': banner,
        'videos':paged_videos,
        'magazines':magazines,
        'events' : events,
        'products' : products,
        'ads' : ads,
        'menu' :menu,
        # 'sub_menu' : sub_menu,
    }
    return render(request,'pages/index.html',context)
    
def about(request):
    author = Author.objects.order_by('hire_date')
    member_author = Author.objects.all().filter(is_member = True)
    context = {
        'author': author,
        'member_author':member_author,
    }
    return render(request,'pages/about.html',context)

def detail(request, article_id):

    article = get_object_or_404(Article, pk = article_id)
    related = Article.objects.all().filter( category = article.category)
    comment = Comment.objects.all().filter(article = article_id)
    recent = Comment.objects.all()[:5]
    menu = Menu.objects.all()
   

    context = {
        'article':article,
        'comment': comment,
        'related': related,
        'recent': recent,
        'menu' :menu,
    }
    return render(request, 'pages/article_detail.html', context)

def nav(request):

    menu = Menu.objects.all()
    print('menuuuu', menu)
    context = {
        'menu' :menu
    }

    return render(request, 'partials/_navbar.html', context)