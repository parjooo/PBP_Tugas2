# Generated by Django 4.1 on 2022-09-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.BooleanField()),
                ('title', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('release_date', models.CharField(max_length=20)),
                ('review', models.TextField()),
            ],
        ),
    ]