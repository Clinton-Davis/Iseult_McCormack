# Generated by Django 3.2 on 2021-04-14 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_inventory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='item_code',
            new_name='code',
        ),
    ]
