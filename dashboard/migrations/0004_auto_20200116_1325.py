# Generated by Django 3.0.2 on 2020-01-16 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20200116_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='image_location',
            new_name='location',
        ),
    ]
