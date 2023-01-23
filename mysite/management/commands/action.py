from django.core.management import BaseCommand
from mysite.models import MailingSetup, MessageForSend, Client, MailingAttempt


class Command(BaseCommand):

    def handle(self, *args, **options):
        mailingsetup = [
            {'time': '12-00', 'period': 'один раз в день', 'sending_status': 'created'},
            {'time': '13-00', 'period': 'один раз в неделю', 'sending_status': 'created'},
            {'time': '14-00', 'period': 'один раз в день', 'sending_status': 'created'},
        ]

        message_for_send = [
            {'title': 'Реклама', 'body': 'Акция в магазине', 'preview': 'Реклама (Акция)', 'mailing': MailingSetup.objects.get(pk=1)},
            {'title': 'Информация', 'body': 'Магазин закрыт', 'preview': 'Информация о магазине', 'mailing': MailingSetup.objects.get(pk=2)},
            {'title': 'Скидки', 'body': 'Распродажа в магазине', 'preview': 'Реклама (Акция)', 'mailing': MailingSetup.objects.get(pk=1)}
        ]

        Clients = [
            {'name': 'Иван', 'email': '1@mail.ru', 'comment': 'Первый'},
            {'name': 'Петр', 'email': '2@mail.ru', 'comment': 'Второй'},
            {'name': 'Василий', 'email': '3@mail.ru', 'comment': 'Третий'},
        ]

        mailingsetup_list = []
        for item in mailingsetup:
            mailingsetup_list.append(MailingSetup(**item))

        MailingSetup.objects.bulk_create(mailingsetup_list)

        message_for_send_list = []
        for item in message_for_send:
            message_for_send_list.append(MessageForSend(**item))

        MessageForSend.objects.bulk_create(message_for_send_list)

        Clients_list = []
        for item in Clients:
            Clients_list.append(Client(**item))

        Client.objects.bulk_create(Clients_list)
