# Generated by Django 2.0.6 on 2018-07-02 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20180702_0108'),
        ('course', '0007_auto_20180701_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='tags',
        ),
        migrations.AddField(
            model_name='link',
            name='tags',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='list',
            name='tags',
        ),
        migrations.AddField(
            model_name='list',
            name='tags',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='summary',
            name='tags',
        ),
        migrations.AddField(
            model_name='summary',
            name='tags',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
