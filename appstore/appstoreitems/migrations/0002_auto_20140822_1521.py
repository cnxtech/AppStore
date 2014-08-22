# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appstoreitems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='appstoreitem',
            name='images',
            field=models.ManyToManyField(to='appstoreitems.AppImage'),
            preserve_default=True,
        ),
    ]
