# Generated by Django 2.0 on 2019-04-16 05:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_auto_20190415_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='structures',
            name='date',
            field=models.DateTimeField(default=datetime.date(2019, 4, 16)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='issued_date',
            field=models.DateTimeField(default=datetime.date(2019, 4, 16)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='return_date',
            field=models.DateTimeField(default=datetime.date(2019, 4, 26)),
        ),
    ]
