# Generated by Django 3.1.1 on 2020-10-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gig', '0010_mygig_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mygig',
            name='time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
