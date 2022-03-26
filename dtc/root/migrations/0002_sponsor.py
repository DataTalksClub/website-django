# Generated by Django 4.0.3 on 2022-03-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('gold', 'gold'), ('silver', 'silver')], max_length=8)),
                ('web_site', models.URLField()),
                ('logo_url', models.URLField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
                ('sort_order', models.IntegerField()),
            ],
        ),
    ]