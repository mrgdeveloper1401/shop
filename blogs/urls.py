from django.urls import include
from rest_framework.urls import path
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

from blogs.views import CategoryViewSet, PostViewSet
router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('post', PostViewSet, basename='post')

category_router = NestedDefaultRouter(router, 'category', lookup='category')
category_router.register('post', PostViewSet, basename='post')


app_name = 'blogs'
urlpatterns = [
    path('', include(router.urls)),
    path('', include(category_router.urls))
    # path('')
]
