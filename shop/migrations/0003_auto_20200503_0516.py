# Generated by Django 2.2.10 on 2020-05-03 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200503_0506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='pictures',
        ),
    ]
