# Generated by Django 3.1.1 on 2020-10-18 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gig', '0018_review_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='Gig.review'),
        ),
    ]
