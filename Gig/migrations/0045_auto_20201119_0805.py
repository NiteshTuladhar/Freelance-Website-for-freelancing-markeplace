# Generated by Django 3.1.1 on 2020-11-19 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gig', '0044_auto_20201102_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10),
        ),
    ]