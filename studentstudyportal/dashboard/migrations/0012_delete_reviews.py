# Generated by Django 4.0.5 on 2022-07-24 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_remove_reviews_user_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]