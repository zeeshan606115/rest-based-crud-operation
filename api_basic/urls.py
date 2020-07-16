from django.urls import path
from .views import articleList, article_detail, article_List, article_detail_api

urlpatterns = [
    path('article', articleList),
    path('article_list', article_List),
    path('article_detail/<int:pk>/', article_detail),
    path('article_detail_api/<int:pk>/', article_detail_api),
]