# Generated by Django 2.1.3 on 2018-11-21 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0028_station_st_live'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='st_tagline',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]