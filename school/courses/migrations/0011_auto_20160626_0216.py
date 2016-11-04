# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_course_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='module',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='text',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='video',
            name='name',
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=150, default='m'),
            preserve_default=False,
        ),
    ]
