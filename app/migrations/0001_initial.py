# Generated by Django 4.2.2 on 2023-07-25 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_price', models.TextField(blank=True, max_length=100, null=True)),
                ('detail_loac', models.TextField(blank=True, max_length=100, null=True)),
                ('flat_loac', models.TextField(blank=True, max_length=100, null=True)),
                ('ph_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('ph_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('ph_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('ph_4', models.ImageField(blank=True, null=True, upload_to='')),
                ('ph_5', models.ImageField(blank=True, null=True, upload_to='')),
                ('iid', models.IntegerField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('flat_name', models.TextField(blank=True, max_length=200, null=True)),
                ('flat_dic', models.TextField(blank=True, max_length=200, null=True)),
                ('num_bed', models.IntegerField(blank=True, max_length=4, null=True)),
                ('num_path', models.IntegerField(blank=True, max_length=4, null=True)),
                ('num_sq', models.IntegerField(blank=True, max_length=20, null=True)),
                ('sub_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('iid', models.IntegerField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
