# Generated by Django 3.1.4 on 2021-01-03 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=60, verbose_name='Email'),
        ),
    ]
