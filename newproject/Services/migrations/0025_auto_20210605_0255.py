# Generated by Django 3.1.7 on 2021-06-04 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0024_auto_20210529_1623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'المستفيد', 'verbose_name_plural': 'المستفيدين'},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': 'الطلبات'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'الخدمات'},
        ),
        migrations.AddField(
            model_name='person',
            name='isseen',
            field=models.BooleanField(default=False),
        ),
    ]
