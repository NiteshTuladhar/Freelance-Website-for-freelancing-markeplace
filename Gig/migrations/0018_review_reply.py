# Generated by Django 3.1.1 on 2020-10-18 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gig', '0017_review_gigs'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='Gig.review'),
        ),
    ]