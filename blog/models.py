from django.db import models
from django.conf import settings


class Blog(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(max_length=200, blank=True, null=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
