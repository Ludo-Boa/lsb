# Generated by Django 5.0.9 on 2024-11-24 20:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_portfoliopage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nom')),
            ],
            options={
                'verbose_name': 'catégorie de projet',
                'verbose_name_plural': 'catégories de projets',
            },
        ),
        migrations.AddField(
            model_name='portfoliopage',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Catégorie du projet', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='portfolio.portfoliocategory'),
        ),
    ]
