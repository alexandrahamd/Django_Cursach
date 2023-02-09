from django.conf import settings
from django.core.cache import cache
from django.http import request

from blog.models import Blog
from mysite.models import Client


def cache_category():
    queryset = Blog.objects.all().order_by('?')[:3]
    if settings.CACHE_ENABLED:
        key = f'Blog_all:{Blog.objects.all()}'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)

        return cache_data
    return queryset


def cache_client(user):
    queryset = Client.objects.filter(user_id=user).count()
    if settings.CACHE_ENABLED:
        key = f'Client_all:{Client.objects.all()}'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)

        return cache_data
    return queryset
