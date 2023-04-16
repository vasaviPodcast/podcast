# Generated by Django 4.2 on 2023-04-14 11:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0006_alter_podcastdetails_uploadedon'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField(default=None)),
            ],
        ),
        migrations.AlterField(
            model_name='podcastdetails',
            name='uploadedOn',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 14, 17, 1, 50, 816345)),
        ),
    ]