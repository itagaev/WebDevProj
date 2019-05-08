# Generated by Django 2.2 on 2019-05-08 15:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190508_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('place', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 5, 8, 15, 24, 40, 651260)),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Patient')),
            ],
        ),
    ]