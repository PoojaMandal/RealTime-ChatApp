# Generated by Django 5.0.4 on 2024-04-26 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='messagefiles/'),
        ),
    ]
