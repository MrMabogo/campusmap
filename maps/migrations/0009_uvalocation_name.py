# Generated by Django 3.1.6 on 2021-04-25 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0008_auto_20210424_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='uvalocation',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
