# Generated by Django 4.0.4 on 2022-06-23 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0012_query_run_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='last_run_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
