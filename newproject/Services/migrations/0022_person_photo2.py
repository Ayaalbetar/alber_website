# Generated by Django 3.1.7 on 2021-05-28 20:44

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0021_auto_20210519_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo2',
            field=models.ImageField(default=2, storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to=''),
            preserve_default=False,
        ),
    ]
