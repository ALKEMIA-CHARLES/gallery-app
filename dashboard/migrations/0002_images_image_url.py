# Generated by Django 3.0.2 on 2020-01-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image_url',
            field=models.URLField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
