# Generated by Django 4.2.9 on 2024-01-16 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_tg_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tg_chat_id',
            field=models.CharField(max_length=10, verbose_name='телеграмм_id'),
        ),
    ]
