# Generated by Django 3.1.1 on 2020-09-30 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0002_auto_20200923_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='category/')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='sub_category/')),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gig.category')),
            ],
        ),
        migrations.CreateModel(
            name='MyGig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('search_tag', models.CharField(max_length=15)),
                ('price', models.FloatField()),
                ('time', models.TimeField(auto_now=True)),
                ('contact_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.myprofile')),
                ('s_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gig.subcategory')),
            ],
        ),
    ]
