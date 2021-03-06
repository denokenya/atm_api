# Generated by Django 3.2.3 on 2021-12-11 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0003_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='ATM_Card',
            fields=[
                ('atm_card_num', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='ATM Card Number')),
                ('name', models.CharField(max_length=100, verbose_name='NAME ON CARD')),
                ('pin', models.IntegerField(verbose_name='PIN')),
                ('date_of_issue', models.DateTimeField(verbose_name='DATE OF ISSUE')),
                ('expiry_date', models.DateTimeField(verbose_name='EXPIRY DATE')),
                ('address', models.CharField(max_length=300, verbose_name='ADDRESS')),
                ('two_factor', models.BooleanField(verbose_name='TWO FACTOR AUTHENTICATION STATUS')),
                ('phone_num', models.BigIntegerField(verbose_name='PHONE NUMBER FOR AUTHENTICATION')),
                ('card_status', models.BooleanField(verbose_name='CARD STATUS')),
                ('account_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atm.account')),
            ],
            options={
                'verbose_name': 'atm card',
                'verbose_name_plural': 'atm cards',
                'db_table': 'atmcard',
                'ordering': ['atm_card_num'],
            },
        ),
    ]
