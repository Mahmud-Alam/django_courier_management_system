# Generated by Django 3.2.6 on 2021-10-19 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_billing_branch_delivery_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]