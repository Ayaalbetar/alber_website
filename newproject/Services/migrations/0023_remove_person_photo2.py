# Generated by Django 3.1.7 on 2021-05-29 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0022_person_photo2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='photo2',
        ),
    ]
