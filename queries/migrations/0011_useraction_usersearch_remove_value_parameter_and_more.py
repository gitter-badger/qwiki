# Generated by Django 4.0.4 on 2022-06-19 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_most_recent_database_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('queries', '0010_delete_userqueryinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('row_id', models.IntegerField()),
                ('action', models.IntegerField()),
                ('table', models.IntegerField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('search', models.CharField(default='', max_length=64)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='value',
            name='parameter',
        ),
        migrations.RemoveField(
            model_name='value',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='value',
            name='user',
        ),
        migrations.AddField(
            model_name='value',
            name='parameter_name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.DeleteModel(
            name='Action',
        ),
    ]
