# Generated by Django 3.1.7 on 2021-04-27 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0016_person_nationalit'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='father_die',
            field=models.BooleanField(default='False'),
        ),
    ]
