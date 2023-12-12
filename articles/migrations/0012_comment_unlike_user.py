# Generated by Django 4.2.7 on 2023-12-10 08:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0011_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='unlike_user',
            field=models.ManyToManyField(related_name='unlike_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]