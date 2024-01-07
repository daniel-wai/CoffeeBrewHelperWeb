# Generated by Django 5.0 on 2023-12-29 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewhelper', '0010_rename_recipe_brewstep_recipeid'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='coffee_grind_size',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='recipe',
            name='coffee_grind_weight',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='temperature',
            field=models.PositiveIntegerField(default=95),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]