# Generated by Django 5.0.4 on 2024-05-11 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_productinventory_first_purchase_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='salescustomerdata',
            name='purchase_qty_in_sqft',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
    ]