# Generated by Django 5.0.6 on 2024-07-02 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_rename_videos_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='src',
            new_name='url',
        ),
    ]
