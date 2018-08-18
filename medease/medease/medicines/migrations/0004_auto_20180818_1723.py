# Generated by Django 2.1 on 2018-08-18 11:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0003_auto_20180731_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Med_Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_cost', models.DecimalField(decimal_places=3, max_digits=10)),
                ('lending_cost', models.DecimalField(decimal_places=3, max_digits=10)),
                ('opening_unit', models.DecimalField(decimal_places=3, max_digits=10)),
                ('recieving_unit', models.DecimalField(decimal_places=3, max_digits=10)),
                ('closing_unit', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='medicines',
            name='closing_unit',
        ),
        migrations.RemoveField(
            model_name='medicines',
            name='company_cost',
        ),
        migrations.RemoveField(
            model_name='medicines',
            name='lending_cost',
        ),
        migrations.RemoveField(
            model_name='medicines',
            name='opening_unit',
        ),
        migrations.RemoveField(
            model_name='medicines',
            name='recieving_unit',
        ),
        migrations.AlterField(
            model_name='client',
            name='cname',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(max_length=11, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.", regex='^\\d{9,10}$')]),
        ),
        migrations.AlterField(
            model_name='med_client_mapper',
            name='client_contact_mapper',
            field=models.ForeignKey(on_delete='models.CASCADE', to='medicines.Client'),
        ),
        migrations.RemoveField(
            model_name='med_client_mapper',
            name='mname_mapper',
        ),
        migrations.AddField(
            model_name='med_client_mapper',
            name='mname_mapper',
            field=models.ManyToManyField(to='medicines.Medicines'),
        ),
        migrations.AddField(
            model_name='med_transaction',
            name='mname_mapper',
            field=models.ForeignKey(on_delete='models.CASCADE', to='medicines.Medicines'),
        ),
    ]
