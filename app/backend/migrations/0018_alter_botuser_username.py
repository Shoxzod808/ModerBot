# Generated by Django 4.0.2 on 2022-09-14 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_alter_botuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
