# Generated by Django 5.0.1 on 2024-02-13 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
