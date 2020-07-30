# Generated by Django 3.0.8 on 2020-07-30 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='kamban',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Date of Create')),
                ('date_change', models.DateField(auto_now=True, verbose_name='Date of Change')),
                ('date_delete', models.DateField(auto_now=True, verbose_name='Date of Delete')),
                ('date_time_c', models.TimeField(auto_now_add=True)),
                ('date_time_m', models.TimeField(auto_now=True)),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='Kamban Step')),
                ('description', models.TextField(blank=True, max_length=600, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Date of Create')),
                ('date_change', models.DateField(auto_now=True, verbose_name='Date of Change')),
                ('date_delete', models.DateField(auto_now=True, verbose_name='Date of Delete')),
                ('date_time_c', models.TimeField(auto_now_add=True)),
                ('date_time_m', models.TimeField(auto_now=True)),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='Name Kamban Step')),
                ('description', models.TextField(blank=True, max_length=600, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Date of Create')),
                ('date_change', models.DateField(auto_now=True, verbose_name='Date of Change')),
                ('date_delete', models.DateField(auto_now=True, verbose_name='Date of Delete')),
                ('date_time_c', models.TimeField(auto_now_add=True)),
                ('date_time_m', models.TimeField(auto_now=True)),
                ('title', models.CharField(max_length=80, verbose_name='task')),
                ('kamban', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='control.kamban')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Date of Create')),
                ('date_change', models.DateField(auto_now=True, verbose_name='Date of Change')),
                ('date_delete', models.DateField(auto_now=True, verbose_name='Date of Delete')),
                ('date_time_c', models.TimeField(auto_now_add=True)),
                ('date_time_m', models.TimeField(auto_now=True)),
                ('title', models.CharField(max_length=80, verbose_name='task')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.Task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Date of Create')),
                ('date_change', models.DateField(auto_now=True, verbose_name='Date of Change')),
                ('date_delete', models.DateField(auto_now=True, verbose_name='Date of Delete')),
                ('date_time_c', models.TimeField(auto_now_add=True)),
                ('date_time_m', models.TimeField(auto_now=True)),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='kamban',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.project'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Date of Create')),
                ('date_change', models.DateField(auto_now=True, verbose_name='Date of Change')),
                ('date_delete', models.DateField(auto_now=True, verbose_name='Date of Delete')),
                ('date_time_c', models.TimeField(auto_now_add=True)),
                ('date_time_m', models.TimeField(auto_now=True)),
                ('comment', models.TextField(max_length=1500)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subtask', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='control.SubTask')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='control.Task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Assigned',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Date of Create')),
                ('date_change', models.DateField(auto_now=True, verbose_name='Date of Change')),
                ('date_delete', models.DateField(auto_now=True, verbose_name='Date of Delete')),
                ('date_time_c', models.TimeField(auto_now_add=True)),
                ('date_time_m', models.TimeField(auto_now=True)),
                ('assigned', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='control.members')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='control.Task')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
