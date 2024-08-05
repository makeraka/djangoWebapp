# Generated by Django 5.0.7 on 2024-08-02 01:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('sold', models.IntegerField(max_length=10000)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)])),
            ],
        ),
    ]
