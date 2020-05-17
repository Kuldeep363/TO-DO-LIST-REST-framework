# Generated by Django 3.0.3 on 2020-05-14 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('complete', models.BooleanField(blank=True, default=False, null=True)),
                ('slugID', models.SlugField(blank=True, default='', null=True)),
            ],
        ),
    ]
