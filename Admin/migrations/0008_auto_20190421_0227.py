# Generated by Django 2.0 on 2019-04-20 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_auto_20190416_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='st_name',
        ),
        migrations.AddField(
            model_name='students',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='students',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='structures',
            name='date',
            field=models.DateTimeField(default=datetime.date(2019, 4, 21)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='issued_date',
            field=models.DateTimeField(default=datetime.date(2019, 4, 21)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='return_date',
            field=models.DateTimeField(default=datetime.date(2019, 5, 1)),
        ),
    ]
