# Generated by Django 3.2 on 2021-04-29 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='fullname',
            new_name='full_name',
        ),
    ]
