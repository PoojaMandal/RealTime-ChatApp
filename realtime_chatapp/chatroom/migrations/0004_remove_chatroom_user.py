# Generated by Django 5.0.4 on 2024-04-26 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0003_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='user',
        ),
    ]
