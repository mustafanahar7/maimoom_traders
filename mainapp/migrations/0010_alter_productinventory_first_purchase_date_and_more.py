# Generated by Django 5.0.4 on 2024-05-11 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_rename_purchase_qty_in_sqft_salescustomerdata_qty_in_sqft_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinventory',
            name='first_purchase_date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='productinventory',
            name='last_purchase_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]