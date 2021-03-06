# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-26 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text=b'Select a genre for this book', to='catalog.Genre'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[(b'm', b'Maintenance'), (b'o', b'On loan'), (b'a', b'Available'), (b'r', b'Reserved')], default=b'm', help_text=b'Book availability', max_length=1),
        ),
    ]
