# Generated by Django 4.2.6 on 2023-10-23 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_shop_ct_shop_image_shop_ot_alter_shop_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='image',
            new_name='img',
        ),
    ]
