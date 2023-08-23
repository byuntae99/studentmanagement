# Generated by Django 3.0.7 on 2023-07-14 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_001', '0018_auto_20230713_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='password',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]