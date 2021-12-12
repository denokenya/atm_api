# Generated by Django 3.2.3 on 2021-12-12 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0005_auto_20211211_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance_Enquiry',
            fields=[
                ('tid', models.IntegerField(primary_key=True, serialize=False, verbose_name='TRANSACTION ID')),
                ('date_time', models.DateTimeField(verbose_name='DATE TIME OF TRANSACTION')),
                ('status', models.CharField(max_length=100, verbose_name='STATUS')),
                ('rescode', models.IntegerField(verbose_name='RESPONSE CODE')),
                ('type_trans', models.CharField(max_length=100, verbose_name='TRANSACTION TYPE')),
                ('bal_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='BALANCE AMOUNT')),
                ('atmcard_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atm.atm_card')),
                ('machine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atm.machine')),
            ],
            options={
                'verbose_name': 'balance enquiry',
                'verbose_name_plural': 'balance enquiries',
                'db_table': 'balanceEnquiry',
                'ordering': ['tid'],
            },
        ),
    ]
