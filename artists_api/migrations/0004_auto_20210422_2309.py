# Generated by Django 3.1.7 on 2021-04-23 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists_api', '0003_auto_20210422_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='albums',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='artist',
            name='tracks',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
