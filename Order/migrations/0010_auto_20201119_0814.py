# Generated by Django 3.1.1 on 2020-11-19 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0009_myorder_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myorder',
            name='completed',
        ),
        migrations.AddField(
            model_name='myorder',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Complete', 'Complete'), ('In Progress', 'In Progress'), ('Cancelled', 'Cancelled')], default='In Progress', max_length=25),
        ),
    ]
