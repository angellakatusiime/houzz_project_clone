# Generated by Django 4.2.2 on 2023-08-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.IntegerField(default='none', max_length=700),
        ),
    ]
