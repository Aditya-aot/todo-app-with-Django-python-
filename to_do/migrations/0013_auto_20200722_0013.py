# Generated by Django 3.0.7 on 2020-07-21 18:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0012_auto_20200719_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 18, 43, 14, 468154, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='last_date',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 18, 43, 14, 469153, tzinfo=utc), null=True),
        ),
    ]
