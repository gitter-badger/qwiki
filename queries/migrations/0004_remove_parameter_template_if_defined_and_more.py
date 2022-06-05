# Generated by Django 4.0.4 on 2022-05-30 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0003_instance_parameter_alter_database_port_value_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parameter',
            name='template_if_defined',
        ),
        migrations.AddField(
            model_name='parameter',
            name='template',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='default',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]