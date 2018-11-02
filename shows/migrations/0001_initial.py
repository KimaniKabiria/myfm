# Generated by Django 2.1.2 on 2018-11-02 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ep_title', models.CharField(max_length=250)),
                ('ep_file_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shw_title', models.CharField(max_length=250)),
                ('shw_hosts', models.CharField(max_length=250)),
                ('shw_icon', models.CharField(max_length=1000)),
                ('shw_station', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_name', models.CharField(max_length=250)),
                ('st_icon', models.CharField(max_length=1000)),
                ('st_freq', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='ep_show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.Show'),
        ),
    ]
