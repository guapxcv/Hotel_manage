# Generated by Django 2.1.3 on 2018-11-25 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20181125_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('work_start_time', models.CharField(max_length=20)),
                ('work_end_time', models.CharField(max_length=20)),
                ('work_weekday', models.CharField(max_length=3)),
                ('date_of_birth', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=1)),
                ('status', models.IntegerField()),
                ('phone_num', models.CharField(max_length=13)),
            ],
        ),
    ]