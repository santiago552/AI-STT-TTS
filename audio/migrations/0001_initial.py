# Generated by Django 5.0.4 on 2024-04-18 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='audios/')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='audios/audio/')),
                ('subtitles', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
