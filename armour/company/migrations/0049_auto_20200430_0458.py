# Generated by Django 2.2 on 2020-04-30 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0048_company_generate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='generate',
            field=models.BooleanField(default=False, verbose_name='Free'),
        ),
    ]