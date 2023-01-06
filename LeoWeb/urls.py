from rest_framework import routers
from django.urls import path,include

from .api import TagViews,ContentViews
from .views import allArticle,SingelArticle,getEmail,success

router=routers.DefaultRouter()
router.register('tag',TagViews,'tag')
router.register('content',ContentViews,'content')

urlpatterns = [
    path('api/',include(router.urls)),
    path('', allArticle.as_view(),name='allArticle'),
    path('get-Email', getEmail.as_view(),name='getEmail'),
    path('success', success.as_view(),name='success'),
    path('<slug:slug>', SingelArticle.as_view(),name='SingelArticle'),
   
    
]
