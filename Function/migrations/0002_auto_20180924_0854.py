# Generated by Django 2.1.1 on 2018-09-24 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Function', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='functions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Function.Function'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=70, unique=True),
        ),
    ]
