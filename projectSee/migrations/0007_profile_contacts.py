# Generated by Django 4.0.5 on 2022-06-12 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectSee', '0006_remove_profile_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contacts',
            field=models.TextField(default='', max_length=100),
        ),
    ]
