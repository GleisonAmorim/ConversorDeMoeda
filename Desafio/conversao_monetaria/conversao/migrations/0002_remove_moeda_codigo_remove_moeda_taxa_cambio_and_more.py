# Generated by Django 5.0.1 on 2024-01-10 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moeda',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='moeda',
            name='taxa_cambio',
        ),
        migrations.AddField(
            model_name='moeda',
            name='cotacao',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='moeda',
            name='nome',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]
