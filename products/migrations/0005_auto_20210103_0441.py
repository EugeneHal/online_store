# Generated by Django 3.1.4 on 2021-01-03 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210103_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_description',
            field=models.CharField(max_length=200, null=True, verbose_name='Category Description'),
        ),
    ]
