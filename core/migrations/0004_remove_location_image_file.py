# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_location_image_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='image_file',
        ),
    ]
