# Generated by Django 2.2 on 2020-02-03 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislation', '0094_auto_20200203_0407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='legistationtopicsresponse',
            name='default',
        ),
        migrations.RemoveField(
            model_name='legistationtopicsresponse',
            name='defaulto',
        ),
        migrations.AddField(
            model_name='sourcenc',
            name='default',
            field=models.BooleanField(default=False, verbose_name='Default to Legal register'),
        ),
        migrations.AddField(
            model_name='sourcenc',
            name='defaulto',
            field=models.BooleanField(default=False, verbose_name='Default to Outer NC'),
        ),
    ]