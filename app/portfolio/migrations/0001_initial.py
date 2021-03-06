# Generated by Django 3.1.6 on 2021-02-21 05:45

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('description', models.CharField(db_index=True, max_length=500)),
                ('icon', models.CharField(blank=True, max_length=50, null=True)),
                ('experience', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('slug', models.CharField(blank=True, db_index=True, max_length=50, null=True)),
                ('client', models.CharField(db_index=True, max_length=50)),
                ('team_size', models.IntegerField()),
                ('description', models.CharField(db_index=True, max_length=500)),
                ('icon', models.CharField(blank=True, max_length=50, null=True)),
                ('completion_date', models.DateField(db_index=True, max_length=50)),
                ('technologies', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), blank=True, default=list, null=True, size=None)),
                ('roles', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), blank=True, default=list, null=True, size=None)),
                ('success', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), blank=True, default=list, null=True, size=None)),
                ('is_feature', models.BooleanField(default=False)),
                ('url', models.CharField(db_index=True, max_length=250)),
                ('github_url', models.CharField(db_index=True, max_length=250)),
                ('image_url', models.CharField(db_index=True, max_length=250)),
                ('background_image_url', models.CharField(db_index=True, max_length=250)),
                ('category', models.ManyToManyField(to='portfolio.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
