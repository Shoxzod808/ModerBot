# Generated by Django 3.2.5 on 2021-11-29 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20211126_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='botuser',
            name='metro',
        ),
        migrations.AlterField(
            model_name='botuser',
            name='url',
            field=models.BooleanField(default=False),
        ),
    ]
