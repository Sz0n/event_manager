# Generated by Django 3.2.4 on 2021-06-27 23:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]