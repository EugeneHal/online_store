# Generated by Django 3.1.4 on 2021-01-05 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20210103_0517'),
        ('orders', '0002_auto_20210103_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='Client'),
        ),
    ]
