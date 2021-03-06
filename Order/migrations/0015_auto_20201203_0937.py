# Generated by Django 3.1.1 on 2020-12-03 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0014_auto_20201129_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myorder',
            name='payment_completed',
        ),
        migrations.AddField(
            model_name='myorder',
            name='payment_complete',
            field=models.CharField(choices=[('Transaction Pending', 'Transaction Pending'), ('Transaction Completed', 'Transaction Completed')], default='Transaction Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='payment_method',
            field=models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('E-Sewa', 'E-Sewa'), ('Khalti', 'Khalti')], default='Cash On Delivery', max_length=50),
        ),
    ]
