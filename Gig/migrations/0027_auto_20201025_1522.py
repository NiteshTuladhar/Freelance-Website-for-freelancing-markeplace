# Generated by Django 3.1.1 on 2020-10-25 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gig', '0026_auto_20201025_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='value',
            field=models.CharField(choices=[('Unlike', 'Unlike'), ('Like', 'Like')], default='Like', max_length=10),
        ),
    ]
