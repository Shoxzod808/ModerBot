# Generated by Django 3.2.5 on 2021-11-20 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_delete_music'),
    ]

    operations = [
        migrations.AddField(
            model_name='botuser',
            name='paid_days',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='botuser',
            name='url',
            field=models.TextField(default=1, max_length=1500),
            preserve_default=False,
        ),
    ]