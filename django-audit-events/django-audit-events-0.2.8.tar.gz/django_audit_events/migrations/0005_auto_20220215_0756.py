# Generated by Django 3.0.11 on 2022-02-15 07:56

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_audit_events', '0004_auto_20210127_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivedauditevent',
            name='headers',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True, verbose_name='Headers'),
        ),
        migrations.AddField(
            model_name='auditevent',
            name='headers',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True, verbose_name='Headers'),
        ),
    ]
