from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(verbose_name='Почта', unique=True)
    username = models.CharField(max_length=200, blank=True, null=True, default=email)
    verify_token = models.CharField(max_length=30, verbose_name='Токен', blank=True, null=True)
    verify_token_expired = models.DateTimeField(blank=True, null=True, verbose_name='Дата истечения токена')
    new_password = models.CharField(verbose_name="новый пароль", max_length=128)
    is_active = models.BooleanField(default=True, verbose_name="статус активации")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


