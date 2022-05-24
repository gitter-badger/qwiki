# Generated by Django 4.0.4 on 2022-05-24 06:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('queries', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Query',
        ),
        migrations.RenameField(
            model_name='query',
            old_name='date_posted',
            new_name='date_created',
        ),
    ]
