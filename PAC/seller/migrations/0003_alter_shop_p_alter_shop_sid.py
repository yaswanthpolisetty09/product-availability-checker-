# Generated by Django 4.2.6 on 2023-10-23 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_remove_shop_pid_remove_shop_pname_remove_shop_qty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='p',
            field=models.TextField(default='unavailable'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='sid',
            field=models.CharField(max_length=1000),
        ),
    ]