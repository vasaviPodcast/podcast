# Generated by Django 4.2 on 2023-04-12 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcastdetails',
            name='uploadedOn',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 12, 23, 27, 58, 314767)),
        ),
    ]