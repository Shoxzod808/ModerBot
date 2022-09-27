# Generated by Django 4.0.2 on 2022-09-14 13:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_botuser_created_botuser_status_botuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='botuser',
            name='status',
        ),
        migrations.AlterField(
            model_name='botuser',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 14, 13, 1, 25, 45652, tzinfo=utc)),
        ),
    ]
