# Generated by Django 3.0.7 on 2023-07-10 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_001', '0013_students_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='file',
            field=models.FileField(default=1, upload_to='file'),
            preserve_default=False,
        ),
    ]
