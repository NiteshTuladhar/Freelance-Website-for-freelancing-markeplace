# Generated by Django 3.1.1 on 2020-10-08 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0016_remove_myprofile_profile_set'),
        ('Gig', '0007_remove_mygig_contact_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='mygig',
            name='contact_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Profile.myprofile'),
        ),
    ]