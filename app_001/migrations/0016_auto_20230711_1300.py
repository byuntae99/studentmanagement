# Generated by Django 3.0.7 on 2023-07-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_001', '0015_auto_20230711_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='imagefiled',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.DeleteModel(
            name='Files',
        ),
    ]