# Generated by Django 4.2.6 on 2023-10-23 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_shop_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='ct',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='shop',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='shop',
            name='ot',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='shop',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='shop',
            name='p',
            field=models.TextField(default=''),
        ),
    ]
