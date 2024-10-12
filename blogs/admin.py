from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin


from blogs.models import Post, Comment, Tag, PostImages, PostCategory


# inline
class PostImagesInline(admin.TabularInline):
    model = PostImages
    extra = 1


# admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['deleted_at', "is_deleted"]
    list_select_related = ['author']
    filter_horizontal = ['tag_name', "category"]
    raw_id_fields = ['author']
    list_display = ['author', "post_title", "show_post_tags", "is_publish", "is_deleted", "post_like"]
    list_editable = ['is_publish']
    search_fields = ['post_title', "author__mobile_phone"]
    prepopulated_fields = {"post_slug": ("post_title",)}
    list_filter = ['created_at', "updated_at", "is_publish"]
    date_hierarchy = 'created_at'
    inlines = [PostImagesInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.prefetch_related('tag_name')
        return qs

    def show_post_tags(self, obj):
        tags = [i.tag_name for i in obj.tag_name.all()]
        return tags


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(PostImages)
class PostImagesAdmin(admin.ModelAdmin):
    pass


@admin.register(PostCategory)
class PostCategoryAdmin(DraggableMPTTAdmin):
    list_select_related = ['parent']
    list_display = ['id', 'category_name', "parent", "is_publish"]
    list_display_links = ['id', 'category_name']
    list_filter = ['is_publish', "created_at", "updated_at"]
    search_fields = ['category_name']
    prepopulated_fields = {'category_slug': ('category_name',)}
