from django.db import models

class MailingSetup(models.Model):
    SENT = "sent"
    NO_SENT = "not sent"
    CREATED = 'created'

    STATUS_CHOICES = [
        (SENT, "Sent"),
        (NO_SENT, "Not sent"),
        (CREATED, 'created')
    ]
    ONE_DAY = "один раз в день"
    ONE_WEAK = "один раз в неделю"
    ONE_MONTH = 'один раз в месяц'

    PERIOD = [
        (ONE_DAY, "один раз в день"),
        (ONE_WEAK, "один раз в неделю"),
        (ONE_MONTH, 'один раз в месяц')
    ]

    time = models.TimeField(blank=True, null=True)
    period = models.CharField(choices=PERIOD, default='UTC', max_length=250, blank=True, null=True)
    sending_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=CREATED)


    def __str__(self):
        return f'Время {self.time}, период {self.period}'


class MessageForSend(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=250, blank=True, null=True)
    preview = models.CharField(max_length=200, blank=True, null=True)
    mailing = models.ForeignKey(MailingSetup, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=250, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class MailingAttempt(models.Model):
    id_message_for_send = models.ForeignKey(MessageForSend, on_delete=models.CASCADE)
    data_time = models.CharField(max_length=150)
    server_response = models.CharField(max_length=250, blank=True, null=True)
    status = models.ForeignKey(MailingSetup, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.id

