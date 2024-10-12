from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey

from core.models import UpdateMixin, CreateMixin, SoftDeleteMixin


class Tag(CreateMixin, UpdateMixin):
    tag_name = models.CharField(_("tag name"))

    def __str__(self):
        return self.tag_name

    class Meta:
        db_table = 'tags'
        verbose_name = _("tag")
        verbose_name_plural = _("tags")


class PostImages(CreateMixin, UpdateMixin):
    post = models.ForeignKey('Post', on_delete=models.PROTECT, related_name='fk_post_images_post')
    image = models.ForeignKey('images.Image', on_delete=models.PROTECT, related_name='fk_post_images_image')
    is_publish = models.BooleanField(default=True)

    class Meta:
        db_table = 'post_image'
        verbose_name = _("post image")
        verbose_name_plural = _("post images")


class PostCategory(MPTTModel, CreateMixin, UpdateMixin):
    category_name = models.CharField(_("category name"), max_length=255)
    category_slug = models.SlugField(_("category slug"), max_length=255, allow_unicode=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, related_name='children', blank=True, null=True)
    is_publish = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name

    class MPTTMeta:
        order_insertion_by = ['category_name']
        db_table = 'post_category'
        verbose_name = _("post category")
        verbose_name_plural = _("post categories")


class Post(CreateMixin, UpdateMixin, SoftDeleteMixin):
    category = models.ManyToManyField('PostCategory', related_name='post_category')
    author = models.ForeignKey("accounts.User", on_delete=models.PROTECT, related_name="posts",
                               limit_choices_to={"is_active": True, "is_staff": True})
    post_title = models.CharField(_("title post"), max_length=100)
    post_slug = models.SlugField(_("post slug"), max_length=100, allow_unicode=True)
    post_body = models.TextField(_("post body"))
    is_publish = models.BooleanField(_("is publish"), default=True)
    post_like = models.PositiveSmallIntegerField(_("post like"), default=0)
    tag_name = models.ManyToManyField(Tag, related_name='post_tags')

    def __str__(self):
        return self.author.mobile_phone

    @property
    def all_image(self):
        image = [i.image.url for i in self.fk_post_images_post.all()]
        return image

    def save(self, *args, **kwargs):
        self.slug = slugify(self.post_title)
        return super().save(*args, **kwargs)

    class Meta:
        db_table = "blog_posts"
        verbose_name = _("post")
        verbose_name_plural = _("posts")


class Comment(CreateMixin, UpdateMixin):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment_body = models.TextField(_("comment body"))
    comment_rate = models.PositiveSmallIntegerField(_('comment rate'), validators=[MinValueValidator(1),
                                                                                   MaxValueValidator(5)])
    is_publish = models.BooleanField(_("is publish"), default=False)
    comment_like = models.PositiveIntegerField(_("comment like"), default=0)
    comment_dislike = models.PositiveIntegerField(_("comment dislike"), default=0)

    def __str__(self):
        return f'{self.post.post_title} {self.is_publish}'

    class Meta:
        db_table = "blog_comments"
        verbose_name = _("comment")
        verbose_name_plural = _("comments")
