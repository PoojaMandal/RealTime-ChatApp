# Generated by Django 5.0.4 on 2024-04-26 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message_attachment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='is_read',
        ),
    ]
