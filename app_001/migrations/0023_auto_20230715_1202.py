# Generated by Django 3.0.7 on 2023-07-15 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_001', '0022_addcourse_staff_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcourse',
            name='staff_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_001.Staff'),
        ),
    ]
