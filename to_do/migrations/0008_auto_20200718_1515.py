# Generated by Django 3.0.7 on 2020-07-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0007_auto_20200718_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='last_date',
            field=models.TextField(),
        ),
    ]