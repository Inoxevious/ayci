from django.conf.urls import url
from django.urls import path, include
from .views import index, signup, home, activate, account_activation_sent, register, logout, login, dashboard
from . import views

# SET THE NAMESPACE!
app_name = 'account'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('dashboard/', dashboard, name = "dashboard"),
    path('login/', login, name = "login"),
    path('logout/', logout, name = "logout"),
    path('register/', register, name = "register"),  


    path('signup/', signup, name='signup'),
    path('index/', index, name='index'),
    path('home/', home, name='home'),
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
]