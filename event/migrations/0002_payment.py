# Generated by Django 3.2.3 on 2021-07-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=122)),
                ('lastname', models.CharField(max_length=122)),
                ('username', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
                ('zip', models.TextField()),
                ('payment', models.TextField()),
                ('cardname', models.CharField(max_length=122)),
                ('cardno', models.TextField()),
                ('expiration', models.TextField()),
                ('cvv', models.TextField()),
            ],
        ),
    ]
