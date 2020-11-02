# Generated by Django 3.1.1 on 2020-11-02 16:20

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0007_myorder_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myorder',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='gig', unique=True),
        ),
    ]
