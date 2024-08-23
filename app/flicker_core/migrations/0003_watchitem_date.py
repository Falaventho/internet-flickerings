# Generated by Django 5.1 on 2024-08-18 14:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flicker_core', '0002_watchitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchitem',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
