# Generated by Django 5.0.4 on 2024-04-18 14:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('educ', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='images')),
                ('phone', models.BigIntegerField()),
                ('dob', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]