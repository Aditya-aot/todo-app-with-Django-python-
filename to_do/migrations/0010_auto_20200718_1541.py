# Generated by Django 3.0.7 on 2020-07-18 10:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0009_auto_20200718_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Last_Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_date', models.TextField(default='yo', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='todo',
            name='last_date',
        ),
        migrations.AddField(
            model_name='todo',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 18, 10, 11, 57, 568311, tzinfo=utc), null=True),
        ),
    ]