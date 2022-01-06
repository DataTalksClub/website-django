# Generated by Django 4.0.1 on 2022-01-06 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0003_alter_event_id_alter_person_socials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('cover_image', models.URLField()),
                ('preview_image', models.URLField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('links', models.JSONField()),
                ('authors', models.ManyToManyField(to='root.Person')),
            ],
        ),
    ]
