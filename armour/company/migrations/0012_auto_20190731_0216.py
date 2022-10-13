# Generated by Django 2.2 on 2019-07-31 02:16

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_companycc_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='billcity',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='company',
            name='billcountry',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='company',
            name='billstreet',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Street'),
        ),
        migrations.AlterField(
            model_name='company',
            name='billzipcode',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='ZIP Code'),
        ),
    ]