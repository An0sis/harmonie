# Generated by Django 4.2.11 on 2024-04-08 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_concert_url_event_url_alter_concert_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='url',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.CharField(max_length=30),
        ),
    ]
