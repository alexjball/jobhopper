# Generated by Django 3.1 on 2020-09-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20200909_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupationtransitions',
            name='occleaveshare',
            field=models.CharField(max_length=50),
        ),
    ]
