# Generated by Django 4.2.2 on 2023-07-26 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='x1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='x2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='y1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='y2',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
