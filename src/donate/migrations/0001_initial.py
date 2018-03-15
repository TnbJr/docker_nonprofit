# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=120, blank=True, null=True)),
                ('last_name', models.CharField(max_length=120, blank=True, null=True)),
                ('donate_email', models.EmailField(max_length=254)),
                ('donation_amount', models.DecimalField(max_digits=20, decimal_places=2)),
                ('donation_comment', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
