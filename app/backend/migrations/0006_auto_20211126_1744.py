# Generated by Django 3.2.5 on 2021-11-26 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20211120_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='botuser',
            name='metro',
            field=models.TextField(default='0'),
        ),
        migrations.AddField(
            model_name='botuser',
            name='owner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='botuser',
            name='price',
            field=models.TextField(default='0'),
        ),
        migrations.AddField(
            model_name='botuser',
            name='rooms',
            field=models.TextField(default='0'),
        ),
        migrations.AlterField(
            model_name='botuser',
            name='url',
            field=models.TextField(default='0'),
        ),
    ]
