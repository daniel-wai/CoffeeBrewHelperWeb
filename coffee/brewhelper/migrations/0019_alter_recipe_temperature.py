# Generated by Django 5.0 on 2024-01-25 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewhelper', '0018_remove_brewmethod_recipes_recipe_methods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='temperature',
            field=models.TextField(default=''),
        ),
    ]
