# Generated by Django 2.0 on 2019-04-20 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_auto_20190421_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
