# Generated by Django 3.1.1 on 2020-10-21 04:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Gig', '0021_auto_20201019_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='mygig',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
