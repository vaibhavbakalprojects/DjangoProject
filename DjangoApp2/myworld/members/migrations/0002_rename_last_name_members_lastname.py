# Generated by Django 4.0.3 on 2022-04-04 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='last_name',
            new_name='lastname',
        ),
    ]
