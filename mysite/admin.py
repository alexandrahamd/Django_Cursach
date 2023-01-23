from django.contrib import admin
from mysite.models import MailingSetup, MessageForSend, Client, MailingAttempt

@admin.register(MailingSetup)
class MailingSetupAdmin(admin.ModelAdmin):
    list_display = ('time', 'period', 'sending_status')


@admin.register(MessageForSend)
class MessageForSendAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ('id_message_for_send', 'data_time', 'server_response','status' )
