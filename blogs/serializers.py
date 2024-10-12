from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField

from accounts import serializers
from blogs.models import Post, PostCategory, Comment, Tag, PostImages


class PostCategorySerializer(ModelSerializer):
    children = SerializerMethodField()

    class Meta:
        model = PostCategory
        fields = ['category_name', "category_slug", "children"]

    def get_children(self, obj):
        child = [i.category_name for i in obj.get_children()]
        return child


class SimpleCategory(ModelSerializer):
    class Meta:
        model = PostCategory
        fields = ['category_name']


class TagNameSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag_name']


class PostImageSerializer(ModelSerializer):
    class Meta:
        model = PostImages
        fields = ['image']


class PostSerializer(ModelSerializer):
    category = SimpleCategory(many=True)
    tag_name = TagNameSerializer(many=True)
    author = CharField(source='author.mobile_phone')
    all_image = SerializerMethodField()

    class Meta:
        model = Post
        fields = ["author", 'post_title', "post_slug", "post_body", 'all_image', "category", "tag_name", "post_like"]

    def get_all_image(self, obj):
        image = [i.image.get_image_address for i in obj.fk_post_images_post.all()]
        return image
