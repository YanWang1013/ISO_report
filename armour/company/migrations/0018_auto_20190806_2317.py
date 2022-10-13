# Generated by Django 2.2 on 2019-08-06 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0017_company_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='currencycompanies', to='legislation.Currency', verbose_name='Currency'),
        ),
    ]