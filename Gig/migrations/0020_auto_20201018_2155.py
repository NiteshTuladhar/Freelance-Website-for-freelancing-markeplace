# Generated by Django 3.1.1 on 2020-10-18 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gig', '0019_auto_20201018_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]