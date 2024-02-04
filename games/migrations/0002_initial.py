# Generated by Django 5.0.1 on 2024-02-04 20:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='players_associated',
            field=models.ManyToManyField(related_name='games', to=settings.AUTH_USER_MODEL),
        ),
    ]
