# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isbn', models.CharField(max_length=30)),
                ('book_title', models.CharField(max_length=200)),
                ('date_of_publication', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='BooksBorrow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_issued', models.DateField()),
                ('date_due_for_return', models.DateField()),
                ('date_returned', models.DateField()),
                ('amount_of_fine', models.IntegerField(default=0)),
                ('book', models.ForeignKey(to='library.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=100)),
                ('book', models.ForeignKey(to='library.Book')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=100)),
                ('user_address', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
                ('email_address', models.EmailField(unique=True, max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='booksborrow',
            name='user',
            field=models.ForeignKey(to='library.User'),
        ),
        migrations.AddField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(to='library.Book'),
        ),
    ]
