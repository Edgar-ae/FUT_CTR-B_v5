# Generated by Django 4.2 on 2023-05-13 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_fut_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='fut',
            name='stage',
            field=models.IntegerField(default=0),
        ),
    ]
