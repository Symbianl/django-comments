# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0003_add_submit_date_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reply_name',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply_to',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='root_id',
            field=models.IntegerField(default=0),
        ),
    ]
