# Generated by Django 4.0.1 on 2022-01-06 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0004_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.SlugField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]