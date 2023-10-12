from django.db import models
from django.utils.translation import gettext_lazy as _



class ProductModel(models.Model):
    en_name = models.CharField(_('English Name'), max_length=100)
    persion_name = models.CharField(_('persion Name'), max_length=100)
    image = models.ImageField(_('Image'))
    price = models.DecimalField(_('Price'), decimal_places=3)
    slug = models.SlugField(_('Slug'), unique=True)
    
    
    def __str__(self) -> str:
        return self.en_name
    
    
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        db_table = 'products'