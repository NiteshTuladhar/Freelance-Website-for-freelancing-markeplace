# Generated by Django 3.1.1 on 2020-11-29 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gig', '0053_auto_20201129_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10),
        ),
    ]
