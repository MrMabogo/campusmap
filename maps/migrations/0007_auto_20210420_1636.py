# Generated by Django 3.1.6 on 2021-04-20 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0006_auto_20210418_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedroute',
            name='name',
            field=models.CharField(default='', max_length=40),
        ),
    ]
