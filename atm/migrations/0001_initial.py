# Generated by Django 3.2.3 on 2021-12-11 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('machine_id', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True, verbose_name='Machine ID')),
                ('location', models.CharField(max_length=200, verbose_name='Location')),
                ('minimum_atm_balance', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Minimum ATM Balance')),
                ('current_balance', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Current Balance')),
                ('last_refill_date', models.DateTimeField(verbose_name='Last Refill Date')),
                ('next_maintenance_date', models.DateTimeField(verbose_name='Next maintenance Date')),
            ],
            options={
                'verbose_name': 'machine',
                'verbose_name_plural': 'machines',
                'db_table': 'machine',
                'ordering': ['machine_id'],
            },
        ),
    ]
