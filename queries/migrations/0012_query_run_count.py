# Generated by Django 4.0.4 on 2022-06-21 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0011_useraction_usersearch_remove_value_parameter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='run_count',
            field=models.IntegerField(default=0),
        ),
    ]
