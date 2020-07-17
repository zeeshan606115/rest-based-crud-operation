from django.urls import path, include
from .views import articleList, article_detail, article_List, \
    article_detail_api, ArticleApiView, ArticleDetails, \
    GenericAPIView, ArticleViewSet, ArticleGenericViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('article', ArticleGenericViewSet, basename='article')
urlpatterns = [
    path('viewset/',include(router.urls) ),
    path('genericviewset/',include(router.urls) ),
    path('viewset/<int:pk>/',include(router.urls) ),
    path('article', articleList),
    path('article_list', article_List),
    path('article_list_class', ArticleApiView.as_view()),
    path('generic/<int:id>/', GenericAPIView.as_view()),
    path('article_detail/<int:pk>/', article_detail),
    path('article_detail_api/<int:pk>/', article_detail_api),
    path('article_detail_class/<int:id>/', ArticleDetails.as_view()),
]