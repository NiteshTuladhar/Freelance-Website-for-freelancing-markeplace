# Generated by Django 3.1.1 on 2020-10-31 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gig', '0037_auto_20201030_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='value',
            field=models.CharField(choices=[('Unlike', 'Unlike'), ('Like', 'Like')], default='Like', max_length=10),
        ),
    ]
