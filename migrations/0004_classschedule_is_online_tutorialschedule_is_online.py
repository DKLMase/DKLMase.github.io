# Generated by Django 5.2 on 2025-04-06 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_classschedule_user_dailytask_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='classschedule',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tutorialschedule',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]
