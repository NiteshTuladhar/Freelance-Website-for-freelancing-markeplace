# Generated by Django 3.1.1 on 2020-10-02 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0010_myprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='full_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
