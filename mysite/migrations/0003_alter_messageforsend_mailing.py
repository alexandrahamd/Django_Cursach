# Generated by Django 4.1.5 on 2023-01-23 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_alter_messageforsend_mailing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageforsend',
            name='mailing',
            field=models.ForeignKey(limit_choices_to={'id': True}, on_delete=django.db.models.deletion.CASCADE, to='mysite.mailingsetup'),
        ),
    ]