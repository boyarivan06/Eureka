# Generated by Django 5.0 on 2024-03-31 20:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0008_merge_0007_alter_idea_description_0007_request'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='abonent',
            new_name='user_to',
        ),
        migrations.RemoveField(
            model_name='request',
            name='author',
        ),
        migrations.RemoveField(
            model_name='request',
            name='text',
        ),
        migrations.AddField(
            model_name='request',
            name='user_from',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='request_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
