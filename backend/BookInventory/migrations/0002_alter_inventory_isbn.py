# Generated by Django 5.0.6 on 2024-09-19 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookInventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='isbn',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
