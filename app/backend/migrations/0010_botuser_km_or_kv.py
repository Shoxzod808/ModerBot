# Generated by Django 3.2.3 on 2021-12-01 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='botuser',
            name='km_or_kv',
            field=models.TextField(default='0'),
        ),
    ]