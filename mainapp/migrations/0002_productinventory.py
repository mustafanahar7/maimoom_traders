# Generated by Django 5.0.4 on 2024-05-08 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('product_code', models.CharField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=70)),
                ('product_category', models.CharField(default=None, max_length=60, null=True)),
                ('product_description', models.TextField(default=None, null=True)),
                ('quantity', models.IntegerField()),
                ('product_image', models.FileField(upload_to='products/')),
                ('cost', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('godown_name', models.CharField(default='Main', max_length=70)),
            ],
        ),
    ]
