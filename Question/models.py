from django.db import models
from django.utils.translation import gettext_lazy as _
from Product.models import ProductModel
from accounts.models import UsersModel


class Comment(models.Model):
    user = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    comment = models.TextField()
    create_at = models.DateTimeField(_('Create at'), auto_now_add=True)
    is_active = models.BooleanField(_('Is active'), default=True)
    image = models.ImageField(_('Image'), null=True, blank=True)
    video = models.FieldFile(_('Video'), null=True, blank=True)
    
    
    def __str__(self) -> str:
        return self.user
    
    
    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        db_table = 'comments'
    
    
class ReplyComment(models.Model):
    user = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    body = models.TextField(_('Body'))
    
    
    def __str__(self) -> str:
        return self.user
    
    
    class Meta:
        verbose_name = _('Reply Comment')
        verbose_name_plural = _('Reply Comments')
        db_table = 'reply_comments'