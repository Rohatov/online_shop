# Generated by Django 5.0.8 on 2024-08-10 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accaunts', '0002_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
