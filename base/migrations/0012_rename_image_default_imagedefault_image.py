# Generated by Django 5.0.9 on 2024-12-03 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_imagedefault'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagedefault',
            old_name='image_default',
            new_name='image',
        ),
    ]
