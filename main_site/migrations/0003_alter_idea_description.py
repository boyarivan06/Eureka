# Generated by Django 5.0 on 2024-01-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0002_tag_user_tags_team_user_teams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='description',
            field=models.CharField(max_length=10),
        ),
    ]
