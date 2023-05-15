from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField('Аватар', upload_to='users_images', null=True, blank=True)
    about_me = models.TextField('О себе.', null=True, blank=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
#
# class Registration(models.Model):
#     userid = models.IntegerField('ID пользователя')
#     password = models.CharField('Пароль', max_length=12)
#     login = models.CharField('Имя пользователя', max_length=20)
#     email = models.CharField('Адрес электронной почты', max_length=50)
#
#     def __str__(self):
#         return self.emails
#
#     class Meta:
#         verbose_name = 'Регистрация'
#         verbose_name_plural = 'Регистрация'
#
#
# class Authorization(models.Model):
#     login = models.CharField('Имя пользователя', max_length=20)
#     password = models.CharField('Пароль', max_length=12)
#
#
#     def __str__(self):
#         return self.login
#
#     class Meta:
#         verbose_name = 'Авторизация'
#         verbose_name_plural = 'Авторизация'
#

# Create your models here.
