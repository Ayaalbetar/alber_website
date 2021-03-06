# Generated by Django 3.1.7 on 2021-03-16 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0003_auto_20210316_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=40)),
                ('pname', models.CharField(max_length=30)),
                ('mname', models.CharField(max_length=40)),
                ('lname', models.CharField(max_length=40)),
                ('phone', models.IntegerField(max_length=10)),
                ('id_namber', models.IntegerField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('place_birth', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('idd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='Services.service_details')),
                ('idperson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='Services.person')),
            ],
        ),
    ]
