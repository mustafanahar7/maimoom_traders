# Generated by Django 5.0.4 on 2024-07-07 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_remove_website_orderitems_is_paid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers_order_from_website',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
