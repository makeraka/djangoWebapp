# Generated by Django 5.0.7 on 2024-08-02 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_listing_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='sold',
            field=models.IntegerField(),
        ),
    ]
