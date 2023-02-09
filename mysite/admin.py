from django.contrib import admin
from mysite.models import MailingSetup, MessageForSend, Client, MailingAttempt


@admin.register(MailingSetup)
class MailingSetupAdmin(admin.ModelAdmin):
    list_display = ('time', 'period', 'sending_status')


@admin.register(MessageForSend)
class MessageForSendAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'active_is', 'last_time_sending')
    available_fields = ()
    hidden_fields = ('active_is',)

    def get_form(self, request, obj, **kwargs):
        if request.user.has_perm('mysite.set_status'):
            self.fields = self.hidden_fields + self.available_fields
        else:
            self.fields = self.available_fields

        return super().get_form(request, obj, **kwargs)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ('id_message_for_send', 'data_time', 'server_response','status' )
