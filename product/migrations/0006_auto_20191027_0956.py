# Generated by Django 2.2.6 on 2019-10-27 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orderproduct',
            new_name='orderproducts',
        ),
    ]
