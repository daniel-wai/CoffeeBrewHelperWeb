# Generated by Django 5.0 on 2024-02-01 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewhelper', '0021_alter_recipe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
    ]
