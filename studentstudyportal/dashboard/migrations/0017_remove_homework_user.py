# Generated by Django 4.0.5 on 2022-08-06 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_remove_notes_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='user',
        ),
    ]
