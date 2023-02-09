from django.db.models import F
from django.shortcuts import render
from django.views.generic import DetailView
from blog.models import Blog


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    # Добавляем счетчик
    def render_to_response(self, *args, **kwargs):
        self.object.views = F('views') + 1
        self.object.save()
        return super().render_to_response(*args, **kwargs)


