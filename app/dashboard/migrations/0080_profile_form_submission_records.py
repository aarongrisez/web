# Generated by Django 2.0.5 on 2018-05-25 21:38

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0079_auto_20180525_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='form_submission_records',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=[]),
        ),
    ]
