# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20160907_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksborrow',
            name='date_due_for_return',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='booksborrow',
            name='date_issued',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='booksborrow',
            name='date_returned',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 8, 8, 25, 7, 610000, tzinfo=utc)),
        ),
    ]
