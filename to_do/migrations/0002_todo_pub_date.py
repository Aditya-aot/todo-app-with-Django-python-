# Generated by Django 3.0.7 on 2020-07-18 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
    ]
