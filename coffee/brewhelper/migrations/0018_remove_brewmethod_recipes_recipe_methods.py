# Generated by Django 5.0 on 2024-01-15 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewhelper', '0017_remove_recipe_methods_brewmethod_recipes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brewmethod',
            name='recipes',
        ),
        migrations.AddField(
            model_name='recipe',
            name='methods',
            field=models.ManyToManyField(related_name='recipes', to='brewhelper.brewmethod'),
        ),
    ]
