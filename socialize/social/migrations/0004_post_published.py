# Generated by Django 5.0.2 on 2024-02-22 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_post_is_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
