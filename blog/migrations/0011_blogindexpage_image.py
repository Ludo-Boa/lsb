# Generated by Django 5.0.9 on 2024-12-03 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_blogpage_image'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Page image Banner', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]