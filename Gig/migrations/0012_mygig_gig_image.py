# Generated by Django 3.1.1 on 2020-10-13 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gig', '0011_auto_20201012_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='mygig',
            name='gig_image',
            field=models.ImageField(blank=True, null=True, upload_to='gig_profile_img'),
        ),
    ]