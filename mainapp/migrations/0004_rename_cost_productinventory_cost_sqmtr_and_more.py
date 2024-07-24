# Generated by Django 5.0.4 on 2024-05-08 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_productinventory_qty_in_metres'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinventory',
            old_name='cost',
            new_name='cost_sqmtr',
        ),
        migrations.RenameField(
            model_name='productinventory',
            old_name='qty_in_metres',
            new_name='qty_sqmtr',
        ),
        migrations.RenameField(
            model_name='productinventory',
            old_name='selling_price',
            new_name='selling_price_sqmtr',
        ),
        migrations.RenameField(
            model_name='productinventory',
            old_name='total_amount',
            new_name='total_amount_sqmtr',
        ),
    ]
