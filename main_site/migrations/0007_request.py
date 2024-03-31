# Generated by Django 4.2.11 on 2024-03-07 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main_site.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0006_idea_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('abonent', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='request_from', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, main_site.models.BaseMethods),
        ),
    ]