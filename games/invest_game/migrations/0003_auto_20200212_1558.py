# Generated by Django 2.2.9 on 2020-02-12 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invest_game', '0002_auto_20200211_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investment',
            name='otherinvested',
        ),
        migrations.RemoveField(
            model_name='investment',
            name='otherreturned',
        ),
        migrations.RemoveField(
            model_name='investment',
            name='points',
        ),
    ]