# Generated by Django 3.1.1 on 2020-10-01 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_remove_myprofile_member_since'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myprofile',
            name='username',
        ),
    ]
