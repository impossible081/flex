# Generated by Django 3.1.2 on 2020-11-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20201118_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phoneNumber',
            field=models.CharField(db_index=True, max_length=11, unique=True),
        ),
    ]
