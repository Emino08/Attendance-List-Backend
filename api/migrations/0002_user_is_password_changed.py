# Generated by Django 4.2.15 on 2024-08-27 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_password_changed',
            field=models.BooleanField(default=False),
        ),
    ]
