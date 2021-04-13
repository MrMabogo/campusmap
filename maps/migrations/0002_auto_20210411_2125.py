# Generated by Django 3.1.6 on 2021-04-12 01:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_email_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('socialaccount', '0003_extra_data_default_dict'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedroute',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='MapUser',
        ),
    ]
