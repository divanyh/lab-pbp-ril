# Generated by Django 4.1 on 2022-09-19 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WatchlistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_status', models.CharField(max_length=7)),
                ('film_title', models.CharField(max_length=255)),
                ('film_rating', models.IntegerField()),
                ('film_release', models.CharField(max_length=17)),
                ('film_review', models.CharField(max_length=280)),
            ],
        ),
    ]