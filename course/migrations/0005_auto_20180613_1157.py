# Generated by Django 2.0.6 on 2018-06-13 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20180613_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='tags',
            field=models.ManyToManyField(blank=True, to='course.Tag'),
        ),
        migrations.AlterField(
            model_name='list',
            name='tags',
            field=models.ManyToManyField(blank=True, to='course.Tag'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='tags',
            field=models.ManyToManyField(blank=True, to='course.Tag'),
        ),
    ]
