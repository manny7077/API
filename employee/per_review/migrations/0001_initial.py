# Generated by Django 4.2.2 on 2023-07-24 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_results', models.CharField(max_length=1000)),
                ('measure', models.CharField(max_length=1000)),
                ('target', models.CharField(max_length=1000)),
                ('weight', models.CharField(blank=True, max_length=1000)),
                ('actual', models.CharField(max_length=1000)),
                ('rating', models.CharField(max_length=1000)),
                ('rating_weight', models.CharField(blank=True, max_length=1000)),
                ('remarks', models.CharField(max_length=1000)),
            ],
        ),
    ]
