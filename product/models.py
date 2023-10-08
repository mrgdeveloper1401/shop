from django.db import models
from django.utils.translation import gettext_lazy as _



class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        db_table = "shop_category"
        ordering = ['name']
        
    def __str__(self) -> str:
        return self.name
    

class SubCategory(models.Model):
    pass


    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        
    def __str__(self) -> str:
        return self.name