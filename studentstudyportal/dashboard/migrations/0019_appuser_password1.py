# Generated by Django 4.0.5 on 2022-08-14 15:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_remove_homework_due_remove_homework_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='password1',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
