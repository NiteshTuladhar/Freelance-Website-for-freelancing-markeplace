# Generated by Django 3.1.1 on 2020-11-02 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gig', '0041_auto_20201031_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='value',
            field=models.CharField(choices=[('Unlike', 'Unlike'), ('Like', 'Like')], default='Like', max_length=10),
        ),
    ]
