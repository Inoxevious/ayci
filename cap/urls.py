"""cap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from Farm.views import farmer
from investmanager.views import investmanager, importer
from account.views import index, signup
from processor.views import processor

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    # urls to user first dashboards
    path('admin/', admin.site.urls),
    # path('', index, name='index'),
    
    path('', signup, name='signup'),
    path('signup', signup, name='signup'),
    path('<int:user_id>/farmer/', farmer, name='farmer'),
    path('<int:user_id>/processor/', processor, name='processor'),
    path('<int:user_id>/investmanager/', investmanager, name='investmanager'),
    
    
   

# urls to applications dashboards
    path('account/', include('account.urls')),
    # urls to applications dashboards
    path('Farm/', include('Farm.urls')),
    path('processor/', include('processor.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url('^searchableselect/', include('searchableselect.urls')),
    
    
    
] 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)