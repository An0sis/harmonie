# Generated by Django 4.2.11 on 2024-04-08 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_events_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='display',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='event',
            name='display',
            field=models.BooleanField(default=True),
        ),
    ]
