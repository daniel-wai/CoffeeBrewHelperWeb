# Generated by Django 5.0 on 2023-12-22 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brewhelper', '0005_alter_brewstep_display_step_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brewstep',
            name='display_step_id',
        ),
    ]
