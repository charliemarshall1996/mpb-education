# Generated by Django 5.2 on 2025-04-17 12:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address_line_1', models.CharField(blank=True, max_length=32, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=32, null=True)),
                ('city', models.CharField(blank=True, max_length=32, null=True)),
                ('county', models.CharField(blank=True, max_length=32, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('guardian', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='students.guardian')),
            ],
        ),
    ]
