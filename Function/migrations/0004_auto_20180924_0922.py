# Generated by Django 2.1.1 on 2018-09-24 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Function', '0003_auto_20180924_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='functions',
            field=models.ManyToManyField(blank=True, to='Function.Function'),
        ),
    ]