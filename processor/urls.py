from django.conf.urls import url
from django.urls import path, include
from .views import RecommendationsView, processor, buyers, investors, home ,  file_manager, market_data, contacts
# SET THE NAMESPACE!
app_name = 'processor'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[

    path('recommends/', RecommendationsView.as_view(), name='recommends'),
    path('buyers/', buyers, name='buyers'),
    path('home/', home, name='home'),
    # path('recommends/', recommends, name='recommends'),
    path('investors/', investors, name='investors'),
    path('market_data/', market_data, name='market_data'),
    path('contacts/', contacts, name='contacts'),
    path('file_manager/', file_manager, name='file_manager'),

]