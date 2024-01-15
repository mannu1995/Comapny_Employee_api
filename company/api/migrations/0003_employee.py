# Generated by Django 5.0 on 2024-01-01 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_company_active_company_added_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('about', models.TextField()),
                ('position', models.CharField(choices=[('Manager', 'manager'), ('Softwer devlopar', 'sd'), ('Project Leader', 'ld')], max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
    ]