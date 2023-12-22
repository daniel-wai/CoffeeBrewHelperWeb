# Generated by Django 5.0 on 2023-12-22 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewhelper', '0003_alter_brewstep_options_brewstep_my_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brewstep',
            old_name='my_order',
            new_name='display_step_id',
        ),
        migrations.AlterField(
            model_name='brewstep',
            name='step_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
