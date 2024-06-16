# Generated by Django 5.0.6 on 2024-06-16 11:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_user', models.TextField()),
                ('message_ai', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('statement', models.CharField(choices=[('BU', 'Бизнес'), ('IN', 'Изобретения'), ('FA', 'Мода')], max_length=2, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
