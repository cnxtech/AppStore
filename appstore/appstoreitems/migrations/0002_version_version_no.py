# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appstoreitems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='version_no',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
