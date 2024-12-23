# Generated by Django 5.0.9 on 2024-11-10 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_socialsettings_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProfileSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(blank=True, verbose_name='date de naissance')),
                ('phone_number', models.CharField(blank=True, max_length=10, verbose_name='numéro de téléphone')),
                ('contact_mail', models.EmailField(blank=True, max_length=254, verbose_name='e-mail de contact')),
                ('highest_degree', models.CharField(choices=[('', 'Selectionnez un niveau'), ('cap', 'CAP'), ('bep', 'BEP'), ('bac', 'BAC'), ('bac+2', 'BAC+2'), ('bac+3', 'BAC+3'), ('bac+4', 'BAC+4'), ('bac+5', 'BAC+5'), ('bac+8', 'BAC+8')], default='cap', max_length=5, verbose_name='diplôme le plus élevé')),
            ],
            options={
                'verbose_name': 'Paramètres de mon profil',
            },
        ),
    ]
