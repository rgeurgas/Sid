# Generated by Django 2.0.6 on 2018-07-02 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=' '),
        ),
    ]
