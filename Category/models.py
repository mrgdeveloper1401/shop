from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.db import models



class CategoryModel(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    slug = models.SlugField(_('Slug'), unique=True)
    create_at = models.DateTimeField(_('create at'), auto_now_add=True)
    update_at = models.DateTimeField(_('update at'), auto_now=True)
    
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categoryies')
        db_table = 'category'
        
        
class SubCategoryModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=100)
    slug = models.SlugField(_('Slug'), unique=True)
    create_at = models.DateTimeField(_('create at'), auto_now_add=True)
    update_at = models.DateTimeField(_('update at'), auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
    
    class Meta:
        verbose_name = _('SubCategory')
        verbose_name_plural = _('SubCategoryies')
        db_table = 'sub_categories'
        