# Generated by Django 3.1.4 on 2021-01-03 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Cart Date / Time Created')),
                ('item_price', models.FloatField(verbose_name='Item Price')),
                ('product_quantity', models.IntegerField(verbose_name='Product(s) Count')),
                ('sub_total', models.FloatField(verbose_name='Sub total')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
                'db_table': 'carts',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Order Date / Time')),
                ('payment_method', models.CharField(max_length=20, verbose_name='Payment method')),
                ('delivery_method', models.CharField(max_length=20, verbose_name='Payment method')),
                ('delivery_date', models.DateTimeField(verbose_name='Delivery Date')),
                ('total_price', models.FloatField(verbose_name='Sub total')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'orders',
            },
        ),
    ]
