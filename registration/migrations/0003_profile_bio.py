# Generated by Django 2.0.6 on 2018-07-02 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_profile_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]