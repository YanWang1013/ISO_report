# Generated by Django 2.2 on 2019-12-23 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('legislation', '0075_auto_20191215_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='legislationtopic',
            name='sq',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specquestionstopics', to='legislation.LegistationSpecQuestion'),
        ),
    ]