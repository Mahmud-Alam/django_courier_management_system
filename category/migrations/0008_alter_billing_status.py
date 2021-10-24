# Generated by Django 3.2.6 on 2021-10-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0007_alter_billing_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='status',
            field=models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='unpaid', max_length=50),
        ),
    ]
