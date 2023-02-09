from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog.models import Blog
from mysite.models import *
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mysite.servises import cache_category, cache_client


class MessageForSendListView(LoginRequiredMixin, ListView):
    model = MessageForSend

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user_id=self.request.user)
        if self.request.user.has_perm('mysite.view_messageforsend'):
            return queryset

        return queryset.filter(active_is=True)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog'] = cache_category()
        context_data['count_active'] = MessageForSend.objects.filter(active_is=True).count()
        context_data['count_all'] = MessageForSend.objects.count()
        context_data['count_uniq_client'] = Client.objects.all().count()
        context_data['count_uniq_mail'] = cache_client(self.request.user)
        return context_data


class MessageForSendUpdateView(UserPassesTestMixin, UpdateView):
    model = MessageForSend
    fields = ('title', 'body', 'preview', 'mailing_id')
    success_url = reverse_lazy('mysite:messageforsend_list')

    def test_func(self):
        message = self.get_object()
        return message.user_id == self.request.user or message.user_id.has_perm('mysite.update_messageforsend')


class MessageForSendCreateView(LoginRequiredMixin, CreateView):
    model = MessageForSend
    fields = ('title', 'body', 'preview', 'mailing_id')
    success_url = reverse_lazy('mysite:messageforsend_list')

    def form_valid(self, form):
        message = form.save(commit=False)
        message.user_id = self.request.user
        message.save()
        return super().form_valid(form)


class MessageForSendDeleteView(UserPassesTestMixin, DeleteView):
    model = MessageForSend
    success_url = reverse_lazy('mysite:messageforsend_list')

    def test_func(self):
        message = self.get_object()
        return message.user_id == self.request.user or message.user_id.has_perm('mysite.delete_messageforsend')


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user_id=self.request.user)
        if self.request.user.has_perm('mysite.view_client'):
            return queryset

        return queryset


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ('name', 'email', 'comment')
    success_url = reverse_lazy('mysite:client_list')

    def form_valid(self, form):
        client = form.save(commit=False)
        client.user_id = self.request.user
        client.save()
        return super().form_valid(form)


class ClientUpdateView(UserPassesTestMixin, UpdateView):
    model = Client
    fields = ('name', 'email', 'comment')
    success_url = reverse_lazy('mysite:client_list')

    def test_func(self):
        client = self.get_object()
        return client.user_id == self.request.user or client.user_id.has_perm('mysite.update_client')


class ClientDeleteView(UserPassesTestMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mysite:client_list')

    def test_func(self):
        client = self.get_object()
        return client.user_id == self.request.user or client.user_id.has_perm('mysite.delete_client')


class MailingAttemptListView(LoginRequiredMixin, ListView):
    model = MailingAttempt
    fields = ('id_message_for_send', 'data_time', 'server_response', 'status')
