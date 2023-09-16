from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class Converter(models.Model):
    """Main model of conversion currency`s pair"""
    
    from_currency = models.CharField(max_length=3, verbose_name='convert from currency')
    to_currency = models.CharField(max_length=3, verbose_name='currency to convert')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created date')
    amount = models.PositiveIntegerField(validators=[MaxValueValidator(9999999)], verbose_name='amount of currency')
    result = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Converter'
        verbose_name_plural = 'Converters'

    def __str__(self):
        return f'{self.from_currency}/{self.to_currency}'


class ConverterSource(models.Model):
    """Model of source data of currencies rates"""
    
    currencies = models.JSONField(verbose_name='all available currencies')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created date')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Source of converter'
        verbose_name_plural = 'Sources of converter'
