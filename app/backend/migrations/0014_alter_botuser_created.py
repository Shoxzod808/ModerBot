# Generated by Django 4.0.2 on 2022-09-14 18:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_remove_botuser_status_alter_botuser_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
