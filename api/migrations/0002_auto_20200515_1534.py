# Generated by Django 3.0.3 on 2020-05-15 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='slugID',
            new_name='taskOwner',
        ),
    ]
