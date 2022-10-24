# Generated by Django 4.0.2 on 2022-09-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_botuser_language_alter_botuser_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='template',
            old_name='text',
            new_name='body_eng',
        ),
        migrations.AddField(
            model_name='template',
            name='body_ru',
            field=models.TextField(default=3),
            preserve_default=False,
        ),
    ]
