# Generated by Django 3.2.3 on 2021-07-21 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='cardno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='cvv',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='expiration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='zip',
            field=models.IntegerField(),
        ),
    ]
