# Generated by Django 3.0.3 on 2020-05-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200518_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='user',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
