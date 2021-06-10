# Generated by Django 3.1.11 on 2021-06-10 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClubUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('l_name', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=50)),
                ('phone_number', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name of Venue')),
                ('address', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=15)),
                ('phone_number', models.CharField(max_length=25)),
                ('web_address', models.URLField(max_length=50)),
                ('email_address', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('manager', models.CharField(max_length=30)),
                ('attendees', models.ManyToManyField(to='home.ClubUsers')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.venue')),
            ],
        ),
    ]