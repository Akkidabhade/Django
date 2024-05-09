# Generated by Django 5.0.4 on 2024-04-29 09:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ARD_BANK', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cunsumer',
            name='amount',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cunsumer',
            name='document',
            field=models.FileField(default=django.utils.timezone.now, upload_to='documents/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cunsumer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
    ]
