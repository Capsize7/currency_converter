from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class Converter(models.Model):
    to_currency = models.CharField(max_length=3, verbose_name='currency to convert')
    from_currency = models.CharField(max_length=3, verbose_name='convert from currency')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created date')
    amount = models.PositiveIntegerField(validators=[MaxValueValidator(9999999)], verbose_name='amount of currency')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Converter'
        verbose_name_plural = 'Converters'

    def __str__(self):
        return f'{self.from_currency}/{self.to_currency}'


class ConverterSource(models.Model):
    currencies = models.JSONField(verbose_name='all available currencies')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created date')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Source of converter'
        verbose_name_plural = 'Sources of converter'
