# Generated by Django 5.0.4 on 2024-05-11 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_rename_cost_sqmtr_productinventory_cost_sqft_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinventory',
            name='first_purchase_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='productinventory',
            name='last_purchase_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.CreateModel(
            name='salesCustomerData',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_address', models.TextField()),
                ('customer_phone_number', models.CharField(max_length=15)),
                ('purchase_date', models.DateField(auto_now=True)),
                ('purchase_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.productinventory')),
            ],
        ),
    ]