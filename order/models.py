from django.db import models

class Tea(models.Model):
    title = models.CharField('Название товара', max_length=66)
    country = models.CharField('Страна производитель', max_length=60)
    impact = models.CharField('Воздействие', max_length=255)
    taste = models.CharField('Вкус', max_length=255)
    price = models.IntegerField('Цена')
    quantity = models.IntegerField('Количество')

    def _str_(selfself):
        return self.title

    class Meta:
        verbose_name = 'Чай'
        verbose_name_plural = 'Список чая'

class Purchases(models.Model):
    subscription = models.CharField('Товар', max_length=50)
    customer_fname = models.CharField('Имя', max_length=50)
    customer_lname = models.CharField('Фамилия', max_length=50)
    paymentmethod = models.CharField('Способ оплаты', max_length=50)
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.subscription

    class Meta:
        verbose_name = 'Покупки'
        verbose_name_plural = 'Покупка'


# Create your models here.
