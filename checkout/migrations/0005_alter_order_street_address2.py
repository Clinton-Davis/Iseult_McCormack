# Generated by Django 3.2 on 2021-06-02 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_country_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, default='', max_length=80, null=True),
        ),
    ]
