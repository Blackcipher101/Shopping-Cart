# Generated by Django 2.2.6 on 2019-10-27 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20191027_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orderproducts',
            new_name='items',
        ),
    ]
