# Generated by Django 3.0.3 on 2020-05-18 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20200515_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='taskOwner',
        ),
        migrations.AddField(
            model_name='tasks',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
