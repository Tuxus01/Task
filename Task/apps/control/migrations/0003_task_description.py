# Generated by Django 3.0.8 on 2020-08-06 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
    ]
