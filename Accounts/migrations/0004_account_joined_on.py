# Generated by Django 3.1.1 on 2020-10-01 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_auto_20200930_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='joined_on',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
