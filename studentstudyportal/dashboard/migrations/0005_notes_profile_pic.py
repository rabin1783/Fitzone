# Generated by Django 4.0.5 on 2022-07-20 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
    ]