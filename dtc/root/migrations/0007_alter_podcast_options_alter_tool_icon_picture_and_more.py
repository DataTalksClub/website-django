# Generated by Django 4.0.3 on 2022-03-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0006_alter_podcast_transcript'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='podcast',
            options={'ordering': ['-season']},
        ),
        migrations.AlterField(
            model_name='tool',
            name='icon_picture',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='links',
            field=models.JSONField(null=True),
        ),
    ]
