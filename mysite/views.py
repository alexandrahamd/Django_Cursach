from django.shortcuts import render
from mysite.models import *
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


class MessageForSendListView(ListView):
    model = MessageForSend

class MessageForSendUpdateView(UpdateView):
    model = MessageForSend
    fields = ('title', 'body', 'preview', 'mailing')
    success_url = reverse_lazy('mysite:messageforsend_list')

class MessageForSendCreateView(CreateView):
    model = MessageForSend
    fields = ('title', 'body', 'preview', 'mailing')
    success_url = reverse_lazy('mysite:messageforsend_list')

class MessageForSendDeleteView(DeleteView):
    model = MessageForSend
    success_url = reverse_lazy('mysite:messageforsend_list')

class ClientListView(ListView):
    model = Client

class ClientCreateView(CreateView):
    model = Client
    fields = ('name', 'email', 'comment')
    success_url = reverse_lazy('mysite:client_list')

class ClientUpdateView(UpdateView):
    model = Client
    fields = ('name', 'email', 'comment')
    success_url = reverse_lazy('mysite:client_list')

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mysite:client_list')

class MailingAttemptListView(ListView):
    model = MailingAttempt
    fields = ('id_message_for_send', 'data_time', 'server_response', 'status')

