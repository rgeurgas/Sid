# Generated by Django 2.0.7 on 2018-07-03 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20180702_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='registration/static/registration/pictures/default.png', upload_to='registration/static/registration/pictures/'),
        ),
    ]
