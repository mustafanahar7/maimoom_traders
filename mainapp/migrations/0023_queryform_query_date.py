# Generated by Django 5.0.4 on 2024-07-22 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_customuser_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='queryform',
            name='query_date',
            field=models.DateField(auto_now=True),
        ),
    ]
