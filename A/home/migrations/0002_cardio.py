# Generated by Django 5.0.4 on 2024-05-08 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cardio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_name', models.CharField(max_length=100)),
                ('callory_burning', models.SmallIntegerField()),
                ('coach', models.CharField(max_length=100)),
            ],
        ),
    ]
