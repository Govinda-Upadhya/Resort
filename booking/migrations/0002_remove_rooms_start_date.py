# Generated by Django 5.0.1 on 2024-01-07 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='start_date',
        ),
    ]
