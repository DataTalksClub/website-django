# Generated by Django 4.0.3 on 2022-03-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_sponsor'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='archive',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
    ]
