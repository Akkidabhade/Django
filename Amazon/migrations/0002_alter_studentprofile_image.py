# Generated by Django 5.0.4 on 2024-04-18 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amazon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
