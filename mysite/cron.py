import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.http import request
from django.utils import timezone
from mysite.models import MailingAttempt, MessageForSend, Client

time_now = datetime.datetime.now()
def send():
    # формируем список клиентов
    emails = []
    for item in Client.objects.filter(user_id=request.user):
        emails.append(item.email)
    for item in MessageForSend.objects.filter(user_id=request.user):
        time_model = item.mailing.time
        title = item.title
        body = item.body
        period = item.mailing.period
        # станавливаем периоды
        if period == "один раз в день":
            item.period_time = 1
        elif period == "один раз в неделю":
            item.period_time = 7
        elif period == 'один раз в месяц':
            item.period_time = 30

        now = time_now.time()
        naive = item.last_time_sending.replace(tzinfo=None)
        # разница между последним изменением и временем на данный момент
        c = time_now - naive

        # если время в модели больше текущего и период, заданный в настройках сообщений,
        # больше разницы между последней отправкой и текущим временем, пытаемся отправить письма

        if time_model >= now and item.period_time >= c.days:
            try:
                send_mail(
                    title,
                    body,
                    settings.EMAIL_HOST_USER,
                    emails,
                    fail_silently=False,
                )
                server_response = '200'
                status = 'Отправлено'

                # устанавливаем новое значение "время отправки последнего письма"
                item.last_time_sending = time_now
            except Exception:
                server_response = '500'
                status = 'Не отправлено'

            new = MailingAttempt.objects.create(
                id_message_for_send=item,
                data_time=timezone.now(),
                server_response=server_response,
                status=status)
            new.save()
    return MailingAttempt
