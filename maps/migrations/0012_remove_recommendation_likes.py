# Generated by Django 3.1.6 on 2021-04-29 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0011_recommendation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendation',
            name='likes',
        ),
    ]
