# Generated by Django 3.0.7 on 2020-07-18 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0006_auto_20200718_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='todo',
            name='last_date',
            field=models.TextField(default='yo', null=True),
        ),
    ]
