# Generated by Django 4.0.5 on 2022-08-06 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_step_delete_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='user',
        ),
    ]
