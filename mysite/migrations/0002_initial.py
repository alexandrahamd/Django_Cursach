# Generated by Django 4.1.5 on 2023-02-09 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageforsend',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mailingattempt',
            name='id_message_for_send',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.messageforsend'),
        ),
        migrations.AddField(
            model_name='client',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]