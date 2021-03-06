# Generated by Django 2.0 on 2019-04-21 23:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_borrows'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrows',
            name='seen_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='structures',
            name='no_of_books',
            field=models.IntegerField(default=2, max_length=1),
        ),
        migrations.AlterField(
            model_name='borrows',
            name='booked_on',
            field=models.DateTimeField(default=datetime.date(2019, 4, 22)),
        ),
        migrations.AlterField(
            model_name='borrows',
            name='valid_till',
            field=models.DateTimeField(default=datetime.date(2019, 4, 23)),
        ),
        migrations.AlterField(
            model_name='structures',
            name='date',
            field=models.DateTimeField(default=datetime.date(2019, 4, 22)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='issued_date',
            field=models.DateTimeField(default=datetime.date(2019, 4, 22)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='return_date',
            field=models.DateTimeField(default=datetime.date(2019, 5, 2)),
        ),
    ]
