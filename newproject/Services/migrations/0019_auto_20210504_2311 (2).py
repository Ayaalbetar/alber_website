# Generated by Django 3.1.7 on 2021-05-04 20:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0018_auto_20210504_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
