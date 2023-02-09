from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('mysite.urls', namespace='mysite')),
    path('users/', include('users.urls', namespace='users')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
]