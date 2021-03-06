# Generated by Django 2.1.1 on 2018-09-24 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('content', models.TextField()),
                ('comment', models.TextField()),
                ('tags', models.CharField(max_length=100)),
                ('slug', models.CharField(blank=True, max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Function',
                'verbose_name_plural': 'Functions',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('functions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Function.Function')),
            ],
        ),
    ]
