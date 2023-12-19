# Generated by Django 4.2.7 on 2023-12-14 06:53

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='content',
        ),
        migrations.AddField(
            model_name='report',
            name='report_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=' '),
        ),
        migrations.AddField(
            model_name='report',
            name='report_title',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='report',
            name='report_user_nickname',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AddField(
            model_name='report',
            name='title',
            field=models.CharField(default=None, max_length=30),
        ),
    ]