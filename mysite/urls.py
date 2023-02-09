from django.urls import path
from mysite.views import *
from . import views
from mysite.apps import MysiteConfig
from django.views.decorators.cache import cache_page

app_name = MysiteConfig.name

urlpatterns = [
    path('', MessageForSendListView.as_view(), name='messageforsend_list'),
    path('client_list/', cache_page(60)(ClientListView.as_view()), name='client_list'),
    path('create_message/', MessageForSendCreateView.as_view(), name='create_message'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('update_client/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('update_message/<int:pk>/', MessageForSendUpdateView.as_view(), name='update_message'),
    path('delete_message/<int:pk>/', MessageForSendDeleteView.as_view(), name='delete_message'),
    path('attempt_list/', cache_page(60)(MailingAttemptListView.as_view()), name = 'attempt_list')
]
