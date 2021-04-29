# Generated by Django 3.1.7 on 2021-04-29 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists_api', '0005_auto_20210425_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='album',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='album',
            name='self_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='tracks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='albums',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='artist',
            name='self_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='tracks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='artist',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='track',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='track',
            name='self_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='times_played',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]