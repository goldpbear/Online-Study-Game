# Generated by Django 2.2.1 on 2019-10-28 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20190912_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='doneinvest',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='investment',
            name='donereturn',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='investment',
            name='respondent',
            field=models.TextField(blank=True, default=' ', null=True),
        ),
    ]