# Generated by Django 5.0.1 on 2024-01-05 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('area_id', models.IntegerField()),
                ('area_name', models.CharField(max_length=64)),
                ('city_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('city_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancy_id', models.CharField(max_length=16, unique=True)),
                ('name', models.TextField()),
                ('salary_from', models.IntegerField(null=True)),
                ('salary_to', models.IntegerField(null=True)),
                ('salary_cur', models.CharField(max_length=16, null=True)),
                ('vac_url', models.URLField()),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blogapp.area')),
                ('skills', models.ManyToManyField(to='blogapp.skill')),
            ],
        ),
    ]