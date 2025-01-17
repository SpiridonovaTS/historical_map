# Generated by Django 5.0 on 2023-12-15 08:02

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CivilizationReference',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoleReference',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CountryReference',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('civilization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shestory.civilizationreference')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('birth_year', models.IntegerField()),
                ('death_year', models.IntegerField(blank=True, null=True)),
                ('nationality', models.CharField(max_length=100)),
                ('achievements', models.TextField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shestory.countryreference')),
                ('roles', models.ManyToManyField(to='shestory.rolereference')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
