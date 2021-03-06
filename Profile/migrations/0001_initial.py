# Generated by Django 3.1.1 on 2020-09-23 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.CharField(blank=True, default='Nepali', max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, null=True)),
                ('full_name', models.CharField(max_length=10, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='user_img/')),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], max_length=30)),
                ('contact_no', models.CharField(max_length=15)),
                ('member_since', models.DateField(auto_now=True)),
                ('skills', models.CharField(blank=True, max_length=100, null=True)),
                ('languages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.language')),
            ],
        ),
    ]
