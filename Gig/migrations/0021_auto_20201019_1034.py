# Generated by Django 3.1.1 on 2020-10-19 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gig', '0020_auto_20201018_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mygig',
            name='created_on',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
