# Generated by Django 3.1.1 on 2020-11-19 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0008_auto_20201102_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorder',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]