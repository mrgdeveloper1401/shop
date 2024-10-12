from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from blogs.models import PostCategory, Post
from blogs.serializers import PostCategorySerializer, PostSerializer


# Create your views here.


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = PostCategory.objects.filter(is_publish=True)
    serializer_class = PostCategorySerializer
    lookup_field = 'category_slug'


class PostViewSet(ReadOnlyModelViewSet):
    lookup_field = 'post_slug'
    serializer_class = PostSerializer
    queryset = (Post.objects.filter(is_publish=True).select_related('author').
                prefetch_related('category', "tag_name", "fk_post_images_post__image"))
    
    def get_queryset(self):
        if self.kwargs:
            return (Post.objects.filter(category__category_slug=self.kwargs['category_category_slug']).filter(is_publish=True).
                    select_related('author').prefetch_related('category', "tag_name", "fk_post_images_post__image"))
        return super().get_queryset()
