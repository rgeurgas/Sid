# Generated by Django 2.0.7 on 2018-07-05 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_merge_20180705_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile/pictures/default.webp', upload_to='profile/pictures/'),
        ),
    ]
