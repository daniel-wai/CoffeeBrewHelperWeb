# Generated by Django 5.0 on 2024-01-15 04:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewhelper', '0015_alter_brewstep_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brewstep',
            name='id',
        ),
        migrations.AlterField(
            model_name='brewstep',
            name='step',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='brewhelper.step'),
        ),
    ]
