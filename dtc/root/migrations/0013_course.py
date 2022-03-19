# Generated by Django 4.0.1 on 2022-01-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0012_tool_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.SlugField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('cover_image', models.URLField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('sylabus', models.JSONField()),
                ('partners', models.JSONField()),
                ('registration_link', models.URLField(blank=True, null=True)),
                ('people', models.ManyToManyField(to='root.Person')),
            ],
        ),
    ]
