# Generated by Django 3.1.6 on 2021-05-04 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0013_auto_20210502_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='address',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
    ]