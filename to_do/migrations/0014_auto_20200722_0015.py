# Generated by Django 3.0.7 on 2020-07-21 18:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0013_auto_20200722_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='last_date',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 18, 45, 36, 864618, tzinfo=utc), null=True),
        ),
    ]
