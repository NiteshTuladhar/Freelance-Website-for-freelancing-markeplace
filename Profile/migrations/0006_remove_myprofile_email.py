# Generated by Django 3.1.1 on 2020-10-01 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0005_auto_20201001_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myprofile',
            name='email',
        ),
    ]
