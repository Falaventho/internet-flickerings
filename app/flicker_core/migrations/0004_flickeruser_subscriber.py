# Generated by Django 5.1 on 2024-08-18 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flicker_core', '0003_watchitem_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='flickeruser',
            name='subscriber',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
