# Generated by Django 4.2 on 2023-06-08 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_fut_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fut',
            name='route',
            field=models.CharField(default='treasury', max_length=50),
        ),
    ]
