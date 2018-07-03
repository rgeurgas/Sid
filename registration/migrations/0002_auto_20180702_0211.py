# Generated by Django 2.0.6 on 2018-07-02 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20180702_0211'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='profile',
            name='courses',
            field=models.ManyToManyField(blank=True, to='course.Course'),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.FileField(default='pictures/mclovin.png', upload_to='pictures/'),
        ),
    ]