# Generated by Django 4.2.7 on 2023-12-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hobbies',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]