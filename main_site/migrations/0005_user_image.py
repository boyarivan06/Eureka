# Generated by Django 4.2.8 on 2024-02-08 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0004_user_votings'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]