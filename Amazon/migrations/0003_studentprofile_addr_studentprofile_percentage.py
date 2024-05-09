# Generated by Django 5.0.3 on 2024-04-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazon', '0002_alter_studentprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='addr',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='percentage',
            field=models.BigIntegerField(default=3),
            preserve_default=False,
        ),
    ]
