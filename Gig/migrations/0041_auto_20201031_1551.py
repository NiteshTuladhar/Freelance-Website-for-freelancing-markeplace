# Generated by Django 3.1.1 on 2020-10-31 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gig', '0040_auto_20201031_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10),
        ),
    ]
