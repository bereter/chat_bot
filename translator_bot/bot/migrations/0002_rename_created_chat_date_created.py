# Generated by Django 5.0.6 on 2024-06-19 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='created',
            new_name='date_created',
        ),
    ]
