# Generated by Django 3.1 on 2020-09-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OccupationTransitions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('soc1', models.CharField(max_length=7)),
                ('soc2', models.CharField(max_length=7)),
                ('total_soc', models.CharField(max_length=9)),
                ('pi', models.CharField(max_length=1)),
                ('occleaveshare', models.CharField(max_length=8)),
            ],
        ),
    ]
