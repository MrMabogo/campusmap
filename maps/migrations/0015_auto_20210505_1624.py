# Generated by Django 3.1.6 on 2021-05-05 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0014_auto_20210504_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedroute',
            name='geojson',
        ),
        migrations.AddField(
            model_name='savedroute',
            name='end',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='savedroute',
            name='start',
            field=models.JSONField(default=dict),
        ),
    ]
