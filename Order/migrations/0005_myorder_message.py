# Generated by Django 3.1.1 on 2020-10-31 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_remove_myorder_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorder',
            name='message',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
