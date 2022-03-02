# Generated by Django 3.2.12 on 2022-03-01 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Xls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('API_WELL_NUMBER', models.IntegerField()),
                ('QUARTER', models.IntegerField()),
                ('OIL', models.IntegerField()),
                ('GAS', models.IntegerField()),
                ('BRINE', models.IntegerField()),
            ],
            options={
                'db_table': 'Xls',
            },
        ),
    ]