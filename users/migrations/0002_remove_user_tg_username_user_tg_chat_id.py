# Generated by Django 4.2.9 on 2024-01-15 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tg_username',
        ),
        migrations.AddField(
            model_name='user',
            name='tg_chat_id',
            field=models.IntegerField(default=1234567890, verbose_name='телеграмм_id'),
            preserve_default=False,
        ),
    ]
