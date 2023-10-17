from django.db import models
from django.utils.translation import gettext_lazy as _

from .api.models import TimeStampModel


class Product(TimeStampModel):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_stock = models.PositiveIntegerField()

    class Meta:
        db_table = 'product'
        verbose_name = _('products')
        verbose_name_plural = _('products')


__all__ = ['Product']
