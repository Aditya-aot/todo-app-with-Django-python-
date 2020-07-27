# Generated by Django 3.0.7 on 2020-07-18 06:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0003_auto_20200718_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='last_date',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 18, 6, 22, 28, 723830, tzinfo=utc), null=True),
        ),
    ]