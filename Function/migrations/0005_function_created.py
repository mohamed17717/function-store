# Generated by Django 2.1.1 on 2018-09-24 22:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Function', '0004_auto_20180924_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='function',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
