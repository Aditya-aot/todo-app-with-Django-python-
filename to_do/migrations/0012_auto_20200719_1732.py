# Generated by Django 3.0.7 on 2020-07-19 12:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0011_auto_20200719_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='last_date',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 19, 12, 2, 34, 331545, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='last_date',
            field=models.TextField(null=True),
        ),
    ]
