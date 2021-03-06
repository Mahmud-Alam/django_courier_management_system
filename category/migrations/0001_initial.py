# Generated by Django 3.2.6 on 2021-10-25 12:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('branch_name', models.CharField(max_length=200, unique=True)),
                ('branch_address', models.TextField(blank=True, null=True, unique=True)),
                ('date_opened', models.DateField(blank=True, null=True)),
                ('branch_revenue', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('category_name', models.CharField(max_length=200, unique=True)),
                ('category_description', models.TextField(blank=True, null=True)),
                ('category_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('category_quantity', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('packaging_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('delivery_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category_vat', models.DecimalField(decimal_places=2, default=5, max_digits=10)),
                ('category_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(default='Order-', max_length=20, primary_key=True, serialize=False, unique=True)),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('customer_phone', models.CharField(blank=True, default='+880', max_length=200, null=True)),
                ('customer_address', models.TextField(blank=True, null=True)),
                ('customer_gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], max_length=50, null=True)),
                ('quantity', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('order_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('recipient_name', models.CharField(max_length=200)),
                ('recipient_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('recipient_phone', models.CharField(blank=True, default='+880', max_length=200, null=True)),
                ('recipient_address', models.TextField(blank=True, null=True)),
                ('recipient_gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], max_length=50, null=True)),
                ('delivery_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('branch_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.branch')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('billing_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=50)),
                ('order_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='category.order')),
            ],
        ),
    ]
